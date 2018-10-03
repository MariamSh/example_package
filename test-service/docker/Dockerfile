FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install Flask=0.10.1

RUN mkdir /app
RUN mkdir /var/log/test_service/

WORKDIR /app

RUN mkdir /app/source_code

COPY ./test-service/ /app/source_code/

ENV PYTHONPATH "&{PYTHONPATH}:/app/source_code"

EXPOSE 64000

