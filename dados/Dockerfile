FROM python:latest

RUN mkdir /dados
WORKDIR /dados

RUN pip install --upgrade pip && \
    pip install requests

ADD . /dados