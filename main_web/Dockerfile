FROM python:3.9-rc-buster
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && python -m pip install --upgrade pip \
    && mkdir /app

WORKDIR /app/

# Install Python Packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
