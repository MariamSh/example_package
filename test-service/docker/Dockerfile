FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install Flask==0.10.1

RUN mkdir /app

WORKDIR /app

RUN mkdir /app/source_code
RUN mkdir /app/logs

COPY ./test-service/ /app/source_code/

ENV PYTHONPATH "&{PYTHONPATH}:/app/source_code"

EXPOSE 64000

CMD ["/bin/bash", "-i", "-c", "/usr/bin/python -u docker.py --host 0.0.0.0 --port 64000 >> /app/logs/test.log"]
