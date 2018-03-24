import requests
import whois
import datetime
from urllib.parse import urlparse
import sys
import os


def load_urls4check(path_to_file):
    with open(path_to_file, 'r') as urls_file:
        for line in urls_file:
            yield line.rstrip()


def get_domain_name(url):
    return urlparse(url).netloc


def is_server_respond_with_ok(url):
    return requests.get(url).ok


def get_domain_expiration_date(domain_name):
    return whois.whois(domain_name)['expiration_date']


def is_enough_days_remained(expiration_date, days=30):
    delta = expiration_date - datetime.datetime.now()
    return delta.days > days


def get_info_about_http_status(url):
    try:
        print('Server name: {}'.format(url))
        if is_server_respond_with_ok(url):
            return 'Server responds'
        else:
            return 'Server does not respond with status HTTP 200'
    except requests.RequestException as e:
        return 'Exception with HTTP status is: {}'.format(e)


def get_info_about_expiration_date(url, days=30):
    try:
        expiration_date = get_domain_expiration_date(get_domain_name(url))
        if is_enough_days_remained(expiration_date, days):
            return 'Server does not expire in {} days'.format(days)
        else:
            return 'Server expires in {} days'.format(days)
    except TypeError:
        return 'Can not get expiration date'


if __name__ == '__main__':
    if len(sys.argv) == 1 or not os.path.isfile(sys.argv[1]):
        sys.exit('Problems with file')
    urls_file = sys.argv[1]
    if len(sys.argv) > 2:
        days = int(sys.argv[2])
    else:
        days = 30
    for url in load_urls4check(urls_file):
        print(50 * '-')
        print(get_info_about_http_status(url))
        print(get_info_about_expiration_date(url, days))
