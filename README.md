# Sites Monitoring Utility

The script checks the status of sites on the following criteria:

* the server responds to the request with the status of HTTP 200;
* the domain name of the site is paid for at least 1 month in advance.

At the input of the script comes a file with a list of url for verification.
Recording format for the URL list:
```
google.com
wikipedia.org
devman.org
pythonforbeginners.com

```
# Get started:

An example of running a script in Linux, Python 3.5:

```bash
$ python3 check_sites_health.py -f domain_list
google.com :
				server respond with status 200 - OK
				the domain name of the site is paid for 938 days
wikipedia.org :
				server respond with status 200 - OK
				the domain name of the site is paid for 1789 days
devman.org :
				server respond with status 200 - OK
				the domain name of the site is paid for 190 days

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
