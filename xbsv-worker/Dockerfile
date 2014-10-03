# XBSV
# version 0.1

From centos7-xbsv:latest
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN useradd -g users buildbot
RUN yum -y install python-devel
RUN easy_install sqlalchemy==0.7.10
RUN easy_install buildbot-slave
RUN mkdir -p /scratch/buildbot
ADD buildbot-xbsv-config.tar.gz /scratch/buildbot/
ADD workername.txt /scratch/buildbot/workername.txt
RUN chown -R buildbot.users /scratch/buildbot
WORKDIR /scratch/buildbot
#RUN buildslave create-slave worker sj9:9989 worker-`cat /scratch/buildbot/workername.txt` xbsv-rules-atomically
#ENTRYPOINT buildslave start worker
