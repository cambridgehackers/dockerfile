# XBSV
# version 0.1

From centos7-xbsv:latest
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN mkdir -p /scratch
RUN useradd -d /scratch/buildbot buildbot && groupmod -g 1010 buildbot && usermod -u 1010 -g 1010 buildbot
RUN yum clean all && yum -y install python-devel connectal
RUN easy_install sqlalchemy==0.7.10
RUN easy_install buildbot-slave
#RUN mkdir -p /scratch/buildbot/.ssh
ADD id_rsa /scratch/buildbot/.ssh/
#ADD id_rsa.pub /scratch/buildbot/.ssh/
#RUN chown buildbot.users /scratch/buildbot/.ssh /scratch/buildbot/.ssh/*
#RUN ls -al /scratch/buildbot/.ssh
RUN chown -R buildbot.users /scratch/buildbot
WORKDIR /scratch/buildbot
ENV HOME /scratch/buildbot
ADD workername.txt /scratch/buildbot/workername.txt
ADD mastername.txt /scratch/buildbot/mastername.txt
RUN mkdir -p /home/buildbot
RUN buildslave create-slave /scratch/buildbot/worker `cat mastername.txt`:9989 worker-`cat workername.txt` xbsv-rules-atomically
RUN cp -r /scratch/buildbot/worker /home/buildbot
RUN chown -R buildbot.buildbot /home/buildbot
ENTRYPOINT twistd -l worker/twistd.log -n -u buildbot -g users -y /scratch/buildbot/worker/buildbot.tac
