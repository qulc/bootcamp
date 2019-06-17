FROM python

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt
