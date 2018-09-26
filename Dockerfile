
FROM continuumio/anaconda3
MAINTAINER olga.botvinnik@czbiohub.org

WORKDIR /home

USER root

# Add user "main" because that's what is expected by this image
RUN useradd -ms /bin/bash main


ENV PACKAGES zlib1g git g++ make ca-certificates gcc zlib1g-dev libc6-dev pigz

WORKDIR /home

RUN apt-get update && \
    apt-get install -y --no-install-recommends ${PACKAGES} && \
    apt-get clean


USER main
