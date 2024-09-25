#!/bin/bash

echo "export DJANGO_SETTINGS_MODULE=pcatia.settings.production" >> ~/.bashrc
echo "export DJANGO_SECRET_KEY='my_secret_key'" >> ~/.bashrc
echo "export DJANGO_DB_NAME='pcatia_db'" >> ~/.bashrc
echo "export DJANGO_DB_USER='pcatia_db_user'" >> ~/.bashrc
echo "export DJANGO_DB_PASSWORD='pg_password'" >> ~/.bashrc
echo "export DJANGO_DB_HOST='pg_host'" >> ~/.bashrc
echo "export DJANGO_DB_PORT='5432'" >> ~/.bashrc

source ~/.bashrc

echo "Variables de entorno agregadas y .bashrc recargado."

cp systemd/gunicorn.service /etc/systemd/system/
cp systemd/gunicorn.socket /etc/systemd/system/
systemctl start gunicorn.socket
systemctl enable gunicorn.socket

echo "Servicio gunicorn activado"
## Luego debe probarse con systemctl status gunicorn.socket
## Chequear la existencia del archivo con file /run/gunicorn.sock
## curl --unix-socket /run/gunicorn.sock localhost
## systemctl status gunicorn


cp nginx/myproject.conf /etc/nginx/sites-available/
echo "Archivo nginx copiado. No olvidar hacer enlace simbolico"


