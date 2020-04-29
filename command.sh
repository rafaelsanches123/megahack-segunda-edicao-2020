#!/bin/bash
cd backend/
# celery multi start worker1 -A project --pidfile="celery.pid" --logfile="celery.log"
python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic --no-input
# gunicorn project.wsgi:application --bind 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000