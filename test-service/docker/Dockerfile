FROM ubuntu:latest

RUN mkdir /app
RUN mkdir /var/log/test_service/

WORKDIR /app

RUN mkdir /app/source_code

COPY ./test-service/ /app/source_code/

ENV PYTHONPATH "&{PYTHONPATH}:/app/source_code"

EXPOSE 64000

