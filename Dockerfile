FROM python:3
ENV PYTHONUNBUFFERED 1
# RUN apt-get update -qq && apt-get install -y python-psycopg2 postgresql-client libpq-dev git-core libmemcached-dev ruby-sass ruby-compass libxml2-dev libxslt1-dev python-dev libjpeg-dev
RUN apt-get update -qq && apt-get install -y locales
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
