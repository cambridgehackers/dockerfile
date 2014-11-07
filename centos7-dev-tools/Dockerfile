From centos:centos7
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>

RUN yum -y upgrade
# xbsv uses the xxd utility, which is part of vim
RUN yum -y groupinstall “Compatibility libraries” "Development tools" && yum -y install fontconfig gcc git libX11 libXft opencv-devel python-setuptools strace tar vim

