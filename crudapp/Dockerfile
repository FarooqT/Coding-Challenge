FROM python:3.6.4

WORKDIR /usr/src/app

COPY requirements.txt ./.

#RUN apt update && apt upgrade -y
RUN pip3 install -r requirements.txt
ADD ./ ./

ENV POSTGRES_NAME=postgres \
    POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=123456 \
    DEBUG=True