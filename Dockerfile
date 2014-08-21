FROM python:2
ENV PYTHONUNBUFFERED 1
RUN apt-get update -qq && apt-get install -y python-psycopg2 postgresql-client libpq-dev git-core libmemcached-dev ruby-sass ruby-compass libxml2-dev libxslt1-dev python-dev libjpeg-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
