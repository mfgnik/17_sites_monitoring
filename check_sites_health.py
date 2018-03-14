import requests
import whois
import datetime
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description='Utility for checking the status of sites'
    )
    parser.add_argument(
        '--file',
        '-f',
        default='domain_list',
        help='path to the file containing domain sites'
    )
    parser.add_argument(
        '--days',
        '-d',
        default=28,
        type=int,
        help='number of days before the end of domain registration'
    )
    return parser.parse_args()


def load_domain4check(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        print('File not found!')
        exit()


def is_server_respond_with_ok(domain):
    try:
        return requests.get(domain).ok
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None


def is_domain_expired(domain, number_days):
    date_now = datetime.datetime.now()
    try:
        domain_info = whois.whois(domain)
    except whois.parser.PywhoisError:
        return None
    expiration_date = domain_info.expiration_date
    if isinstance(domain_info.expiration_date, list):
        expiration_date = domain_info.expiration_date[0]
    elif domain_info.expiration_date is None:
        return None
    return (expiration_date - date_now).days > number_days


def check_site_status(domain, number_days):
    site_status = {}
    if is_server_respond_with_ok(domain):
        site_status.update({'respond': 'OK'})
    else:
        site_status.update({'respond': 'NO CONNECT'})
    domain_extended = is_domain_expired(domain, number_days)
    if domain_extended is None:
        site_status.update({'domain_extended': 'NO DATA'})
    elif not domain_extended:
        site_status.update({'domain_extended': 'NOT EXTENDED'})
    else:
        site_status.update({'domain_extended': 'OK'})
    return site_status


if __name__ == '__main__':
    args = get_args()
    number_days = get_args().days
    domain_list = load_domain4check(args.file)
    print('\nCheck the status of the site from {}'.format(args.file))
    for domain in domain_list:
        site_status = check_site_status(domain, number_days)
        print(domain)
        print ('Respond status - {}'.format(site_status['respond']))
        print('Domain extended  more than {} days : {}'.format(
            number_days, site_status['domain_extended']
            ))
        print('-'*80)
