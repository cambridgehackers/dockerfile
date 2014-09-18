# XBSV
# version 0.1

From centos:centos6
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>

ADD openttdcoop.repo /etc/yum.repos.d/openttdcoop.repo
ADD synnefo.repo /etc/yum.repos.d/synnefo.repo
RUN mkdir -p /scratch/bluespec /scratch/Xilinx/Vivado
RUN yum -y groupinstall “Compatibility libraries”
RUN yum -y groupinstall "Development tools"
RUN yum -y install gcc
# RUN yum -y install flash-plugin nspluginwrapper curl
RUN yum -y upgrade
RUN yum -y install python-ply
RUN yum -y install python-argparse
RUN yum -y install tar
RUN yum -y install git
# RUN yum -y install graphviz graphviz-tcl
# RUN yum -y install ftp
RUN useradd xbsv
VOLUME /scratch/bluespec
VOLUME /scratch/Xilinx
RUN git clone git://github.com/cambridgehackers/xbsv /scratch/xbsv
RUN chown -R xbsv.xbsv /scratch/xbsv
ENV PATH $PATH:/scratch/bluespec/Bluespec-2014.07.A/bin
ENV BLUESPECDIR /scratch/bluespec/Bluespec-2014.07.A/lib

