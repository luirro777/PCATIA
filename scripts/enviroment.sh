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

