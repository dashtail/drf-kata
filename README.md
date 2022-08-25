# drf-kata


## Background

Here at SewerAI we use Django to power our primary API. Django is a web framework which by default is mostly used to serve HTML. It also features a powerful ORM for interacting with databases. Django Rest Framework is an addon library which facilitates the creation of JSON REST APIs within Django. 

Documentation can be found at:

Django: https://docs.djangoproject.com/en/3.2/

DRF: https://www.django-rest-framework.org/
## How to use this Kata

You are given a bootstrap for Django and Postgres with Django Rest Framework also installed.

Your goal is to create a simple note taking API.

## Kata: Note endpoint and suggested schema

First and foremost, feel free to change the suggested schema. It may not be ideal.

### Endpoints

`GET /notes/`

`GET /notes/<id>/`

`POST /notes/`

`PATCH /notes/<id>/`

`DELETE /notes/<id>/`

### Note Schema

```
id
subject
text
```

## Requirements

Your app should run an API with all of the above endpoints functional. Please use the features of DRF to accomplish this -- your app should utilize serializers and viewsets. Your endpoints should require authentication. Also add functionality to the Django admin page to show your models. Writing unit tests is optional.

## Getting started

    docker-compose up

The compose creates a volume in the base directory and will automatically refresh the server as you make code changes.

You can open a shell into the container as follows:

    docker exec -it {container_name} bash

Run the migrations to generate the database

    python manage.py mimgrate

Within that shell you can run the python manage command. You can create an admin user with:

    python manage.py createsuperuser --email admin@example.com --username admin



## End to End Testing

Provide us with some mechanism for testing the above endpoints.

e.g. 
```
curl --location --request POST 'http://localhost:8000/notes/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMzMyNjA1LCJqdGkiOiIyMDJiOGVmNWQzMjg0YjhlYTExZWUyNjk1N2VmZDcwMCIsInVzZXJfaWQiOjI3LCJwcm9maWxlIjp7InNpZCI6IjU4NjQ1ZDIzLTU1NzgtNGYzYy04N2U5LTdlYjAzZDA3MmE0ZiJ9fQ.OfeOIRBWp0yIuFg7Er_GrwPPshozyxAaB_pxiKfRSGM
--data-raw '{   
    "subject": "My First Note",
    "text": "It's the first one",
}'
```
To run the tests, use the following command:

    docker exec {container_name} python manage.py test

