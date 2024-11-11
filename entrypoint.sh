#!/bin/sh

set -e

echo "Chequeando el estado de las migraciones..."
if ! python manage.py showmigrations | grep '\[ \]'; then
  echo "Aplicando migraciones..."
  python manage.py migrate
else
  echo "No hay migraciones pendientes."
fi

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando servidor..."
exec "$@"
