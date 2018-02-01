# Bootcamp

[![Build Status](https://travis-ci.org/qulc/bootcamp.svg?branch=master)](https://travis-ci.org/qulc/bootcamp)
[![CircleCI](https://circleci.com/gh/qulc/bootcamp/tree/master.svg?style=svg)](https://circleci.com/gh/qulc/bootcamp/tree/master)
[![codecov](https://codecov.io/gh/qulc/bootcamp/branch/master/graph/badge.svg)](https://codecov.io/gh/qulc/bootcamp)

Bootcamp is an open source **social network** built with [Python][0] using the [Django Web Framework][1].

## Demo: 
[https://bootcamp.qulc.me/][2]
![](http://i.imgur.com/pGS1kRd.png)

## Fork Features
* Add unittest and show coverage
* Migrate from Python 2 to Python 3.6
* Code style pep8 format
* Add [Travi CI][3] auto test and deploy to [heroku][4]
* Change allow guest user access
* Internationalization add Chinese support
* Upgrade Django to lastest version

## Doing
* Add cache optimization
* Optimization search

## Install Guide
```bash
$ git clone https://github.com/qulc/bootcamp.git
$ cd bootcamp/

# Use Python 3.6 virtualenv or pyenv
$ python -m venv {VENV} && source venv/bin/activate
$ python -m pip install -r requirements.txt

# Add DATABASE_URL, REDIS_URL config to env
$ export REDIS_URL=redis://localhost:6379/0
$ export DATABASE_URL=postgres://postgres:@localhost:5432/bootcamp

# Create Tables
$ python manage.py makemigrations
$ python manage.py migrate

# Test
$ python manage.py test

# Run
$ python manage.py collectstatic
$ python manage.py runserver
```

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://bootcamp.qulc.me/
[3]: https://travis-ci.org/
[4]: https://www.heroku.com
