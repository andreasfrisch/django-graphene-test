# GraphQL test setup

This is not meant to be developed into a production ready anything.

Based on: https://stackabuse.com/building-a-graphql-api-with-django/


## Setup

Create a virtual environment

	python3 -m venv env
	source env/bin/activate

Install requirements.py

	pip install -r requirements.py

Create and make migrations

	python manage.py makemigrations
	python manage.py migrate

Load data fixtures

	python manage.py loaddata movies.json

Start the server

	python manage.py runserver


## GraphiQL Interface

When the server is running visit

	http://localhost:8000/graphql/