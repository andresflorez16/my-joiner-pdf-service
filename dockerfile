#FROM alpine:latest
FROM python:3.10.13-alpine

RUN apk update
#RUN apk add py-pip
#RUN apk add --no-cache python3 py3-pip
#RUN pip install --upgrade pip

WORKDIR /app
ADD . /app

RUN cd /app && pip3 install -r requirements.txt

CMD ["python3", "app.py"]
