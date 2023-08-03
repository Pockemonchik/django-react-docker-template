#!/bin/sh
# mount external dirs
echo "Migrate...";
python manage.py makemigrations --noinput;
python manage.py migrate --noinput;
echo "Createsuperuser...";
python manage.py createsuperuser --noinput;
exec "$@"