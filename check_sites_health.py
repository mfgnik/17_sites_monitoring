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


def is_server_respond_with_ok(url):
    try:
        return requests.get(url).ok
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None


def is_payment_expire(url, paid_days):
    date_now = datetime.datetime.now()
    try:
        domain_info = whois.whois(url)
    except whois.parser.PywhoisError:
        return None
    expiration_date = domain_info.expiration_date
    if type(domain_info.expiration_date) is list:
        expiration_date = domain_info.expiration_date[0]
    elif domain_info.expiration_date is None:
        return 'No data'
    return (expiration_date - date_now).days > paid_days


def check_site_status(url, paid_days):
    site_status = {}
    if is_server_respond_with_ok(url):
        site_status.update({'respond': 'OK'})
    else:
        site_status.update({'respond': 'NO CONNECT'})
    payment_expire = is_payment_expire(url, paid_days)
    if payment_expire == 'No data':
        site_status.update({'payment': 'NO DATA'})
    elif payment_expire is None:
        site_status.update({'payment': 'NO CONNECT'})
    elif not payment_expire:
        site_status.update({'payment': 'NO PAY'})
    else:
        site_status.update({'payment': 'OK'})
    return site_status


if __name__ == '__main__':
    argv = get_argv()
    paid_days = get_argv().paiddays
    domain_list = load_urls4check(argv.file)
    if domain_list:
        print('\nCheck the status of the site from {}'.format(argv.file))
        for url in domain_list:
            site_status = check_site_status(url, paid_days)
            print(url)
            print ('Respond status - {}'.format(site_status['respond']))
            print('Paid period more than {} days : {}'.format(
                paid_days, site_status['payment']
            ))
            print('----------------------------------------------------------')
    else:
        print('File not found')
