# Mi aplicación en django

Una aplicación de python lista para ejecutar en Heroku.

## Ejecutar en local

Debes tener instalado Python 3.9 [instalar](https://docs.python-guide.org/starting/installation/).

```sh
$ cd django

$ python3 -m venv django
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ python manage.py runserver
```

Tu aplicación debe iniciar en [localhost:5000](http://localhost:5000/).

## Ejecutando en Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
o

[![Iniciar](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentación

Más información de uso de Python en Heroku:

- [Python en Heroku](https://devcenter.heroku.com/categories/python)
