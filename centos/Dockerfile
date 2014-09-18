# XBSV
# version 0.1

From centos:centos6
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>

ADD openttdcoop.repo /etc/yum.repos.d/openttdcoop.repo
ADD synnefo.repo /etc/yum.repos.d/synnefo.repo
RUN mkdir -p /scratch/bluespec /scratch/Xilinx/Vivado
RUN cat /etc/centos-release
# RUN find /scratch/xbsv
RUN yum -y groupinstall “Compatibility libraries”
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
# ADD Bluespec-2014.07.A.tar.gz /scratch/bluespec/Bluespec-2014.07.A
# ADD Vivado-2014.1.tar.gz /scratch/Xilinx/Vivado/2014.1
# RUN rpm -qa

