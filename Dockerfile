FROM python:3.7-slim

RUN apt-get update && apt-get install build-essential -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

RUN apt-get install -y nodejs \
    npm
