#!/bin/sh
set -e

# Wait for DB to be ready
: "${MYSQL_HOST:=db}"
: "${MYSQL_PORT:=3306}"

echo "Waiting for database $MYSQL_HOST:$MYSQL_PORT..."

# simple loop to wait for DB
while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  echo "Waiting for MySQL at $MYSQL_HOST:$MYSQL_PORT..."
  sleep 1
done

echo "Database is available."

# Aplicar migraciones (sin interactive)
python manage.py makemigrations --noinput || true
python manage.py migrate --noinput

# Collect static (opcional en dev)
# python manage.py collectstatic --noinput

# Ejecutar el comando pasado al contenedor
exec "$@"