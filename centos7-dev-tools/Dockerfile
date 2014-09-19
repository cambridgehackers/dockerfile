From centos:centos7
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>

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
RUN yum -y install strace
# xbsv uses the xxd utility, which is part of vim
RUN yum -y install vim
RUN easy_install ply
