FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get clean all

MAINTAINER Joelson A Santos "joelsonn.santos@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /work
WORKDIR /work

RUN apt-get install -y libsqlite3-dev wget python-pip build-essential pkg-config python-dev && \
	pip install --upgrade pip && \
	pip install pandas && \
	pip install -U drf-yasg && \
	pip install psycopg2 && \
	pip install qrcode[pil] && \
	pip install Django && \
	pip install argparse && \
	pip install joblib && \
	pip install djangorestframework && \
	pip install markdown==3.0 && \	
	pip install django-filter && \
	pip install gunicorn && \
	pip install pymongo && \
	pip install pillow && \
	pip install whitenoise && \
	pip install celery && \
	pip install oauth2_provider && \
	pip install pytest-django && \
	pip install pytest && \
	pip install greenlet && \
	pip install nose

ADD . /work/
