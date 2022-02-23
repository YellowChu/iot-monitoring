FROM node:16-alpine as nodebuilder

WORKDIR /code

COPY . /code/

RUN npm --prefix frontend install
RUN npm --prefix frontend run build


FROM python:3.10.2-slim

RUN apt-get update && apt-get install build-essential -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=nodebuilder /code/ /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD daphne asgi:application --bind 0.0.0.0 --port $PORT
