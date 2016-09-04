# Bootcamp

[![Build Status](https://travis-ci.org/qulc/bootcamp.svg?branch=master)](https://travis-ci.org/qulc/bootcamp)
[![codecov](https://codecov.io/gh/qulc/bootcamp/branch/master/graph/badge.svg)](https://codecov.io/gh/qulc/bootcamp)

Bootcamp is an open source **social network** built with [Python][0] using the [Django Web Framework][1].

## Demo: 
[https://bootcamp.qulc.me/][2]
![](http://i.imgur.com/pGS1kRd.png)

## Fork Features
* Add Unittest
* Migrate to python3
* Code style pep8 format
* Change use guest access
* Update Django to lastest version
* Internationalization add Chinese support
* Use [Travi CI][3] auto test and deploy to [heroku][4]

## Doing
* Add cache optimization

## Install Guide
```bash
$ git clone https://github.com/qulc/bootcamp.git
$ cd bootcamp/

# Use Python3 virtualenv
$ pyvenv venv && source venv/bin/activate 
$ pip install -r requirements.txt

# Create Tables
$ python manage.py makemigrations
$ python manage.py migrate

# Run
$ python manage.py runserver
```

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://bootcamp.qulc.me/
[3]: https://travis-ci.org/
[4]: https://www.heroku.com
