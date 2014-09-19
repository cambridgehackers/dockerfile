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
## RUN easy_install ply
## RUN easy_install argparse
RUN yum -y install python-ply
RUN yum -y install python-argparse
RUN yum -y install tar
RUN yum -y install git
# RUN yum -y install graphviz graphviz-tcl
# RUN yum -y install ftp
RUN useradd xbsv
VOLUME /scratch/bluespec
VOLUME /scratch/Xilinx
VOLUME /scratch/android-ndk-r9d
RUN git clone git://github.com/cambridgehackers/xbsv /scratch/xbsv
WORKDIR /scratch/xbsv
RUN git pull
RUN git clone git://github.com/cambridgehackers/fpgamake /scratch/fpgamake
WORKDIR /scratch/fpgamake
RUN git pull
RUN git clone git://github.com/cambridgehackers/buildcache /scratch/buildcache
WORKDIR /scratch/buildcache
RUN git pull
WORKDIR /
RUN chown -R xbsv.xbsv /scratch/xbsv
ENV BLUESPECDIR /scratch/bluespec/Bluespec-2014.07.A/lib
ENV PATH $PATH:/scratch/bluespec/Bluespec-2014.07.A/bin:/scratch/android-ndk-r9d:/scratch/Xilinx/Vivado/2014.1/bin

