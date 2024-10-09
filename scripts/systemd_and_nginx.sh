#!/bin/bash

cp systemd/gunicorn.service /etc/systemd/system/
cp systemd/gunicorn.socket /etc/systemd/system/
systemctl start gunicorn.socket
systemctl enable gunicorn.socket

echo "Servicio gunicorn activado"
## Luego debe probarse con systemctl status gunicorn.socket
## Chequear la existencia del archivo con file /run/gunicorn.sock
## curl --unix-socket /run/gunicorn.sock localhost
## systemctl status gunicorn


cp nginx/pcatia.conf /etc/nginx/sites-available/
echo "Archivo nginx copiado. No olvidar hacer enlace simbolico"


