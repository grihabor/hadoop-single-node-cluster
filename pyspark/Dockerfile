FROM ubuntu:18.04

RUN apt-get update -y && apt-get install vim -y && apt-get install wget -y && apt-get install ssh -y && apt-get install openjdk-8-jdk -y && apt-get install sudo -y

RUN apt-get install -y python3-pip

RUN pip3 install --upgrade pip wheel \
 && pip3 install pyspark

WORKDIR /pyspark

ADD run.py .
ADD core-site.xml config/core-site.xml
ADD yarn-site.xml config/yarn-site.xml

ENV HADOOP_CONF_DIR /pyspark/config

ENTRYPOINT python3 run.py
