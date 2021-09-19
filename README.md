# **DRF API CRM system**  

## **Inroduction**

It is the CRM system which provides of the interaction of Organizations, Workers, Clietns, Orders which built with Django-Rest-Framework.  
More about system funcionality you can read in [docs/index.md](./docs/index.md)  

## **Installation**

* Install pipenv - `python3 -m pip install pipenv`
* Establish and activate the virtual environment(recommend use python3)  
  In python3 you can do that with `pipenv shell`
* Install all necessary libraries `pipenv install`  
* Install all migrations `pipenv run python3 manage.py makemigrations && python3 manage.py migrate`
* Do not forget to create a superuser account `pipenv run python3 manage.py createsuperuser`  

## **Testing**

Right now still unrealized API tests and all tests of Client application. Tests of serializers and models is all that you can testing.

For start testing run command `pipenv run python3 manage.py test`  

## **Running**  

For running you just need run `pipenv run python3 manage.py runserver`
