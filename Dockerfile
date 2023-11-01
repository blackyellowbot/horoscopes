FROM python:3.11-slim

WORKDIR /src
COPY requirements.txt /src
#RUN pip install -r -y requirements.txt
RUN PYTHONPATH=/usr/bin/python pip install -r requirements.txt
COPY . /src
