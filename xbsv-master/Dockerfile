# XBSV
# version 0.1

From centos7-dev-tools:latest
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN mkdir -p /scratch
RUN useradd -d /scratch/buildbot -g users buildbot
ADD master.cfg /scratch/buildbot/master.cfg
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
EXPOSE 8080
RUN buildbot create-master master
RUN ls -al /scratch/buildbot
