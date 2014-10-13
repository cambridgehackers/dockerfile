# XBSV
# version 0.1

From centos7-xbsv:latest
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN mkdir -p /scratch
RUN useradd -d /scratch/buildbot -g users buildbot
RUN ls -al /scratch/buildbot
RUN yum -y install python-devel
RUN easy_install sqlalchemy==0.7.10
RUN easy_install buildbot-slave
RUN mkdir -p /scratch/buildbot/.ssh
ADD buildbot-xbsv-config.tar.gz /scratch/buildbot/
ADD workername.txt /scratch/buildbot/workername.txt
ADD id_rsa /scratch/buildbot/.ssh/
ADD id_rsa.pub /scratch/buildbot/.ssh/
RUN chown buildbot.users /scratch/buildbot/.ssh /scratch/buildbot/.ssh/*
RUN ls -al /scratch/buildbot/.ssh
RUN chown -R buildbot.users /scratch/buildbot
WORKDIR /scratch/buildbot
#RUN buildslave create-slave worker sj9:9989 worker-xg10 xbsv-rules-atomically
#ENTRYPOINT buildslave start worker
