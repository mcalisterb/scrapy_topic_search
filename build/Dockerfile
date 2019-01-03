FROM ubuntu:xenial

#RUN sudo apt-get install -y --no-install-recommends python2.7
RUN apt-get update && apt-get install -y --no-install-recommends python3-pip
RUN apt-get install -y --no-install-recommends build-essential autoconf libtool python3-dev python3-setuptools
RUN pip3 install --upgrade pip
RUN pip3 install scrapy-wayback-machine

RUN apt-get install -y --no-install-recommends vim
RUN ls
RUN mkdir /scrapy_project/
RUN cd /scrapy_project/ && scrapy startproject scrapy_topic_search
COPY ./src/spiders/*.py /scrapy_project/scrapy_topic_search/scrapy_topic_search/spiders/
COPY ./src/settings.py /scrapy_project/scrapy_topic_search/scrapy_topic_search/
COPY ./src/search_results_to_hit_count.py /scrapy_project/
COPY ./src/run_service.sh /scrapy_project/

#CMD touch /tmp/test.log && tail -f /tmp/test.log
CMD bash /scrapy_project/run_service.sh

RUN mkdir /mnt/search_outputs/
VOLUME /mnt/search_outputs/
