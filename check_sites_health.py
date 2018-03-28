import requests
import whois
import datetime
from urllib.parse import urlparse
import sys
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_path',
        help='path to the file with urls',
        required=True
    )
    parser.add_argument(
        '--days',
        type=int,
        default=30,
        help='amount of days to check'
    )
    return parser.parse_args()


def load_urls4check(path_to_file):
    with open(path_to_file, 'r') as urls_file:
        for line in urls_file:
            yield line.rstrip()


def get_domain_name(url):
    return urlparse(url).netloc


def is_server_respond_with_ok(url):
    return requests.get(url).ok


def get_domain_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name)['expiration_date']
    if type(expiration_date) == list:
        return expiration_date[0]
    return expiration_date


def is_enough_days_remained(expiration_date, days=30):
    if expiration_date is None:
        return None
    delta = expiration_date - datetime.datetime.now()
    return delta.days > days


def get_info_about_site(url, days):
    server_name = 'Server name: {}'.format(url)
    try:
        server_respond_info = 'Server responds with ok: {}'.format(
            is_server_respond_with_ok(url)
        )
    except requests.RequestException as e:
        server_respond_info = 'Exception with HTTP status is: {}'.format(e)
    expiration_date = get_domain_expiration_date(get_domain_name(url))
    expiration_date_info = 'Server does not expire in {} days: {}'.format(
        days, not is_enough_days_remained(expiration_date, days))
    return server_name, server_respond_info, expiration_date_info


if __name__ == '__main__':
    arguments = parse_args()
    if not os.path.isfile(arguments.input_path):
        sys.exit('Problems with file')
    for url in load_urls4check(arguments.input_path):
        print(50 * '-')
        print(*get_info_about_site(url, arguments.days), sep='\n')
