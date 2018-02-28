import requests
import whois
import datetime
import argparse


def get_argv():
    parser = argparse.ArgumentParser(
        description='Utility for checking the status of sites'
    )
    parser.add_argument(
        '--file',
        '-f',
        default='domain_list',
        help='path to the file containing url sites',
    )
    parser.add_argument(
        '--paiddays',
        '-p',
        default=28,
        type=int,
        help='paid days'
    )
    return parser.parse_args()


def load_urls4check(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        return None


def is_server_respond_with_200(url):
    if requests.get(url).ok:
        return True


def get_domain_expiration_date(url):
    date_now = datetime.datetime.now()
    try:
        domain_info = whois.whois(url)
        expiration_date = domain_info.expiration_date
        if type(domain_info.expiration_date) is list:
            expiration_date = domain_info.expiration_date[0]
        elif domain_info.expiration_date is None:
            return None
        paid_days = (expiration_date - date_now).days
        return paid_days
    except whois.parser.PywhoisError:
        return None


def check_site_status(url, paid_days):
    if is_server_respond_with_200(url):
        expiration_date = get_domain_expiration_date(url)
        if expiration_date > paid_days:
            return True


if __name__ == '__main__':
    argv = get_argv()
    paid_days = get_argv().paiddays
    domain_list = load_urls4check(argv.file)
    if domain_list:
        print('Check the status of the site from {}'.format(argv.file))
        for url in domain_list:
            if check_site_status(url, paid_days):
                print('{} - OK'.format(url))
            else:
                print('{} - HAS PROBLEMS'.format(url))
    else:
        print('File not found')
