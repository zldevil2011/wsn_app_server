#! /bin/bash
source /home/devil/django/app_server_virtual/bin/activate
ps -ef|grep app_server/uwsgi|grep -v grep|cut -c 9-15|xargs kill -9
uwsgi --ini /home/devil/django/app_server_virtual/wsn_app_server/app_server/uwsgi.ini
