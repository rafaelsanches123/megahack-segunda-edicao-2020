#!/bin/bash
# celery multi start worker1 -A project --pidfile="celery.pid" --logfile="celery.log"
python backend/manage.py makemigrations
python backend/manage.py migrate
# python manage.py collectstatic --no-input
# gunicorn project.wsgi:application --bind 0.0.0.0:8000
python backend/manage.py runserver 0.0.0.0:8000