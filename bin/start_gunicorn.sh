#!/bin/bash
cd /home/gobest/django-rest-api/restapi
pipenv run gunicorn restapi.wsgi:application --bind 62.109.11.4:8000

