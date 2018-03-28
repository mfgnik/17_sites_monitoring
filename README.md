# Sites Monitoring Utility

Script gets files with urls and print info about it's HTTP status and expiration date.

# How to install

You should install packages from requirements.txt

```bash

pip install requirements.txt

```

# Quick start

```bash
python sites_monitoring.py -h
usage: sites_monitoring.py [-h] --input_path INPUT_PATH [--days DAYS]

optional arguments:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH
                        path to the file with urls
  --days DAYS           amount of days to check
 ```
 ```bash
python sites_monitoring.py --input_path urls.txt --days 100
--------------------------------------------------
Server name: http://pep8online.com
Server responds with ok
Server does not expire in 100 days
--------------------------------------------------
Server name: https://www.avito.ru/
Server responds with ok
Server expires in 100 days
--------------------------------------------------
Server name: https://www.sports.ru/
Server responds with ok
Server expires in 100 days
--------------------------------------------------
Server name: https://habrahabr.ru/
Server responds with ok
Server does not expire in 100 days
--------------------------------------------------
Server name: https://www.km20.ru/
Server responds with ok
Server does not expire in 100 days
--------------------------------------------------
Server name: https://github.com/
Server responds with ok
Can not get expiration date
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
