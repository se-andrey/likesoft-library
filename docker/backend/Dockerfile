FROM python:3.8.15-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./likesoft /app/likesoft
COPY ./docker /app/docker

RUN chmod +x /app/docker/backend/server-entrypoint.sh
RUN chmod +x /app/docker/backend/worker-entrypoint.sh
