FROM python:3.9-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --proxy http://210.245.31.15:80

ENV HTTP_PROXY="http://proxy.fpt.vn:80"
ENV http_proxy="http://proxy.fpt.vn:80"
ENV HTTPS_PROXY="http://proxy.fpt.vn:80"
ENV https_proxy="http://proxy.fpt.vn:80"
ENV NO_PROXY="localhost,172.0.0.1,0.0.0.0"
ENV no_proxy="localhost,172.0.0.1,0.0.0.0"