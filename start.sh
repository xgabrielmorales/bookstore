#!/bin/bash

# Migrations
/usr/local/bin/python manage.py makemigrations
/usr/local/bin/python manage.py migrate

# Initialize the server
/usr/local/bin/python manage.py runserver 0.0.0.0:$PORT
