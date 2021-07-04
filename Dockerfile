FROM python:3.8

ENV PYTHONBUFFERED 1
RUN mkdir /coinmena
WORKDIR /coinmena

COPY . .

RUN pip install -r requirements.txt
