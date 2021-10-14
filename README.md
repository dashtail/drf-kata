# drf-kata

## How to use this Kata

You are given a bootsrap for Django and Postgres with Django Rest Framework also installed.

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

## Getting started

docker-compose up

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
