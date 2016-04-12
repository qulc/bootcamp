FROM ubuntu:latest

RUN sed -i 's/archive/cn.archive/g' /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y build-essential python python-dev python-pip libjpeg-dev libmysqlclient-dev && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . /app/
WORKDIR /app/

RUN pip install -r requirements.txt -i http://pypi.douban.com/simple/

CMD mkdir -p /data/media/ /data/log/ && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    uwsgi bootcamp.ini

