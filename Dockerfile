
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

ARG slug
ENV slug ${slug:jhcepas/eggnog-mapper}

RUN conda create -n eggnog-mapper-env python=2.7
RUN conda activate eggnog-mapper-env
RUN git clone https://github.com/${slug}.git@${branch}
RUN cd eggnog-mapper && pip install .
RUN ./download_eggnog_data.py -y all


USER main
