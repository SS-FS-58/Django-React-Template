FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /server
WORKDIR /server
COPY server/requirements.txt /server/requirements.txt
RUN pip install -r requirements.txt
COPY server /server