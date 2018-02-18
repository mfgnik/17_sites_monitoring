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
    return parser.parse_args()


def load_urls4check(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        return None


def is_server_respond_with_200(url):
    if requests.get('http://www.{}'.format(url)).ok:
        return '200 ОК'


def get_domain_expiration_date(domain_name):
    data_now = datetime.datetime.now()
    try:
        domain_inf = whois.whois(domain_name)
        expiration_date = domain_inf.expiration_date
        if type(domain_inf.expiration_date) is list:
            expiration_date = domain_inf.expiration_date[0]
        elif domain_inf.expiration_date is None:
            return 'No data'
        expiration_numbers_days = (expiration_date - data_now).days
        return expiration_numbers_days
    except whois.parser.PywhoisError:
        return 'No data'


def print_domain_inf(url):
    print(url, ':')
    server_respond_with_200 = 'OK'
    if is_server_respond_with_200(url) is None:
        server_respond_with_200 = 'Fall'
    print('\t\t\t\tserver respond with status 200 - {}'.format(server_respond_with_200))
    domain_expiration_date = get_domain_expiration_date(url)
    print('\t\t\t\tthe domain name of the site is paid for {} days'.format(domain_expiration_date))


if __name__ == '__main__':
    path_file = get_argv()
    domain_list = load_urls4check(path_file.file)
    if domain_list:
        for domain_url in domain_list:
            print_domain_inf(domain_url)
    else:
        print('File not found')
