FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /cutlink
WORKDIR /cutlink
COPY requirements.txt /cutlink/
RUN pip install -r requirements.txt
COPY . /cutlink/