#!/bin/bash

echo "export DJANGO_SETTINGS_MODULE=pcatia.settings.production" >> ~/.bashrc
echo "export DJANGO_SECRET_KEY='Iephoa2liek$ait/oh^w<u2sheicheeth2ua7thaofoong6que'" >> ~/.bashrc
echo "export DJANGO_DB_NAME='pcatia_db'" >> ~/.bashrc
echo "export DJANGO_DB_USER='pcatia_db_user'" >> ~/.bashrc
echo "export DJANGO_DB_PASSWORD='Wieshoa3tofei[thoo6oog9ieshae2'" >> ~/.bashrc
echo "export DJANGO_DB_HOST='pg_host'" >> ~/.bashrc
echo "export DJANGO_DB_PORT='5432'" >> ~/.bashrc

source ~/.bashrc

echo "Variables de entorno agregadas y .bashrc recargado."

