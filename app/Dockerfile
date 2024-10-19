FROM docker.io/python:3.14.0a1-slim-bookworm

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
    apt-get install -y gcc libpq-dev postgresql

RUN mkdir -p /app/src
WORKDIR /app

COPY src/ src
COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

