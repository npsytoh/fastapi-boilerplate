FROM python:3.12-bookworm

RUN apt-get update \
  && apt-get upgrade

WORKDIR /app
COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app/

EXPOSE 8000
