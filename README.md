# foodgram-project
[![foodgram_workflow](https://github.com/vamotest/foodgram-project/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/vamotest/foodgram-project/actions/workflows/foodgram_workflow.yml)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

## Описание
**foodgram** — база кулинарных рецептов. Пользователи могут создавать 
свои рецепты, читать рецепты других пользователей, подписываться 
на интересных авторов, добавлять лучшие рецепты в избранное, 
а также создавать список покупок и получать его в txt формате. 

## Локальное использование

1) Создаем `.env` и заполняем переменные окружения:

```shell
vim .env
```
```text
SECRET_KEY=
DEBUG=
DJANGO_ALLOWED_HOSTS=
DEFAULT_FROM_EMAIL=
DB_ENGINE=
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
```


2) Устанавливаем [Docker](https://docs.docker.com/engine/install/)

3) Собираем `docker-compose` в detach mode (background):
```shell
docker-compose up --build -d --force-recreate
```

4) Собираем статические файлы в `STATIC_ROOT`:
```shell
docker-compose exec web python3 manage.py collectstatic --noinput
```

5) Запускаем миграции:
```shell
docker-compose exec web python3 manage.py migrate --noinput
```

6) Наполняем `Postgres` данными:
```shell
docker-compose exec web python3 manage.py loaddata fixture.json
```

7) Останавливаем и удаляем контейнеры, сети, тома и образы:
```shell
docker-compose down -v --remove-orphans
```

## Стек технологий
- Python 3.8
- Django and Django Rest Framework
- PostgreSQL
- Gunicorn + Nginx
- CI/CD: Docker, docker-compose, GitHub Actions
- Yandex.Cloud