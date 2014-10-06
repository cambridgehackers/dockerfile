# XBSV
# version 0.1

From centos7-dev-tools:latest
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN mkdir -p /scratch
RUN useradd -d /scratch/buildbot -g users buildbot
RUN ls -al /scratch/buildbot
RUN yum -y install python-devel
RUN easy_install sqlalchemy==0.7.10
RUN easy_install buildbot
RUN mkdir -p /scratch/buildbot/.ssh
ADD buildbot-xbsv-config.tar.gz /scratch/buildbot/
ADD id_rsa /scratch/buildbot/.ssh/
ADD id_rsa.pub /scratch/buildbot/.ssh/
RUN chown buildbot.users /scratch/buildbot/.ssh /scratch/buildbot/.ssh/*
RUN ls -al /scratch/buildbot/.ssh
RUN chown -R buildbot.users /scratch/buildbot
WORKDIR /scratch/buildbot
USER buildbot
EXPOSE 8080 9989
RUN buildbot create-master master
ADD master.cfg /scratch/buildbot/master/master.cfg
ADD projects.py /scratch/buildbot/master/projects.py
ADD projects.json /scratch/buildbot/master/projects.json
ADD root.html /scratch/buildbot/master/templates/root.html
ADD projects.html /scratch/buildbot/master/templates/projects.html
RUN ls -al /scratch/buildbot
