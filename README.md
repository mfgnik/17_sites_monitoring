# Sites Monitoring Utility

The script checks the status of sites on the following criteria:

* the server responds to the request with the status of HTTP 200;
* the domain name of the site is paid for at least 1 month in advance.

At the input of the script comes a file with a list of url for verification.
Recording format for the URL list:
```
http://www.google.com
http://www.wikipedia.org
http://www.devman.org
http://www.pythonforbeginners.com

```
# Get started:

An example of running a script in Linux, Python 3.5:

```bash
$ python3 check_sites_health.py -f domain_list -p 28

Check the status of the site from domain_list
https://wikipedia.org
Respond status - OK
Paid period more than 28 days : OK
--------------------------------------------------------------------------
https://wikipcwioncebvuibnvjib2qinkoscjiqedia.org
Respond status - NO CONNECT
Paid period more than 28 days : NO DATA
--------------------------------------------------------------------------
```
Used arguments:
```bash
-f [--file] - path to the file containing url sites
-p [--paiddays] - number of paid days for the site's domain name
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
