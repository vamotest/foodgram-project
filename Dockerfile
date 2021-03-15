FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/web

RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev \
    && apk add --no-cache musl-dev jpeg-dev zlib-dev \
    && apk add --no-cache --virtual .build-deps build-base linux-headers

COPY ./requirements.txt ./

RUN python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir \
    && rm requirements.txt

WORKDIR $APP_HOME
COPY . $APP_HOME

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000