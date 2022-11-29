FROM python:3.11-slim-buster

RUN apt-get update && apt-get -y install libpq-dev gcc

ENV APP_DB_HOST_PORT=$APP_DB_HOST_PORT
ENV APP_DB_NAME=$APP_DB_NAME
ENV APP_DB_USER=$APP_DB_USER
ENV APP_DB_PASSWORD=$APP_DB_PASSWORD

WORKDIR /app

COPY ./requirements.txt .
COPY ./app.py .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]

