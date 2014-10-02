From centos:centos7
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>

RUN yum -y groupinstall “Compatibility libraries”
RUN yum -y groupinstall "Development tools"
RUN yum -y install gcc
# RUN yum -y install flash-plugin nspluginwrapper curl
RUN yum -y upgrade
RUN yum -y install tar
RUN yum -y install git
# RUN yum -y install graphviz graphviz-tcl
# RUN yum -y install ftp
RUN yum -y install strace
# xbsv uses the xxd utility, which is part of vim
RUN yum -y install vim
RUN yum -y install python-setuptools
RUN easy_install ply
RUN yum -y install libX11
RUN yum -y install libXft
RUN yum -y install fontconfig
