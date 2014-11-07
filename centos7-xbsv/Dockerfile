# CONNECTAL
# version 0.2

From centos7-dev-tools
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN useradd -g users connectal
ADD connectal.repo /etc/yum.repos.d/connectal.repo
RUN yum -y install connectal android-tools
## fix up a couple of things
#ADD flexlmrc /home/connectal/.flexlmrc
ADD Xilinx.lic /home/connectal/.Xilinx/Xilinx.lic
RUN ln -s /usr/lib64/libgmp.so.10.1.1 /usr/lib64/libgmp.so.3
ENV BLUESPECDIR /scratch/bluespec/Bluespec-2014.05.beta1/lib
ENV PATH $PATH:/scratch/bluespec/Bluespec-2014.05.beta1/bin:/scratch/android-ndk-r9d:/scratch/Xilinx/Vivado/2014.1/bin
ENV HOME /home/connectal
ENV CONNECTALDIR /usr/share/connectal
VOLUME /home/connectal/work
WORKDIR /home/connectal/work

RUN chown -R connectal.users /home/connectal
