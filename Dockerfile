FROM ubuntu:latest

RUN sed -i 's/archive/cn.archive/g' /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y build-essential python3 python3-dev libjpeg-dev libmysqlclient-dev && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

CMD mkdir -p /data/media/ /data/log/ && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py collectstatic --noinput && \
    uwsgi bootcamp.ini
