import requests
import whois
import datetime
from urllib.parse import urlparse
import sys


def load_urls4check(path_to_file):
    with open(path_to_file, 'r') as urls_file:
        for line in urls_file:
            yield line.rstrip()


def get_domain_name(url):
    return urlparse(url).netloc


def is_server_respond_with_200(url):
    return requests.get(url).ok


def get_domain_expiration_date(domain_name):
    return whois.query(domain_name).__dict__['expiration_date']


def month_remained(expiration_date):
    month = 30
    delta = expiration_date - datetime.datetime.now()
    return delta.days > month


def get_info_about_http(url):
    try:
        print('Server name: {}'.format(url))
        if is_server_respond_with_200(url):
            print('Server responds with status HTTP 200')
        else:
            print('Server does not respond with status HTTP 200')
    except requests.RequestException as e:
        print('Exception with HTTP status is: {}'.format(e))


def get_info_about_expiration_date(url):
    try:
        expiration_date = get_domain_expiration_date(get_domain_name(url))
        if month_remained(expiration_date):
            print('Server does not expire in month')
        else:
            print('Server expires in month')
    except TypeError:
        print('Can not get expiration date')


if __name__ == '__main__':
    urls_file = sys.argv[1]
    for url in load_urls4check(urls_file):
        print(50 * '-')
        get_info_about_http(url)
        get_info_about_expiration_date(url)
