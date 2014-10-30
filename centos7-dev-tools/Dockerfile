From centos:centos7
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>

RUN yum -y groupinstall “Compatibility libraries”
RUN yum -y groupinstall "Development tools"
# xbsv uses the xxd utility, which is part of vim
RUN yum -y install fontconfig gcc git libX11 libXft opencv-devel python-setuptools strace tar vim
# RUN yum -y install flash-plugin nspluginwrapper curl
RUN yum -y upgrade
RUN easy_install ply
