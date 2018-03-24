# Sites Monitoring Utility

Script gets files with urls and print info about it's HTTP status and expiration date.

# How to install

You should install packages from requirements.txt

```bash

pip install requirements.txt

```

# Quick start

```bash
python sites_monitoring.py urls.txt 100
--------------------------------------------------
Server name: http://pep8online.com
Server responds
Server does not expire in 100 days
--------------------------------------------------
Server name: https://www.avito.ru/
Server responds
Server expires in 100 days
--------------------------------------------------
Server name: https://www.sports.ru/
Server responds
Server expires in 100 days
--------------------------------------------------
Server name: https://habrahabr.ru/
Server responds
Server does not expire in 100 days
--------------------------------------------------
Server name: https://www.km20.ru/
Server responds
Server does not expire in 100 days
--------------------------------------------------
Server name: https://github.com/
Server responds
Can not get expiration date
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
