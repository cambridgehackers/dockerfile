# XBSV
# version 0.1

From centos7-dev-tools
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN useradd -g users connectal
ADD xbsv.repo /etc/yum.repos.d/connectal.repo
RUN yum -y install connectal
RUN yum -y install android-tools
## fix up a couple of things
RUN chmod agu+rx /usr/share/connectal/scripts/*.py
RUN sed -i 's|IPDIR=$(CONNECTALDIR)/out|IPDIR=$(HOME)/.connectal/out|' /usr/share/connectal/Makefile.connectal
RUN sed -i 's|../..|$(CONNECTALDIR)|' /usr/share/connectal/examples/*/Makefile
ADD flexlmrc /home/connectal/.flexlmrc
ADD Xilinx.lic /home/connectal/.Xilinx/Xilinx.lic
RUN ln -s /usr/lib64/libgmp.so.10.1.1 /usr/lib64/libgmp.so.3
ENV BLUESPECDIR /scratch/bluespec/Bluespec-2014.05.beta1/lib
ENV PATH $PATH:/scratch/bluespec/Bluespec-2014.05.beta1/bin:/scratch/android-ndk-r9d:/scratch/Xilinx/Vivado/2014.1/bin
ENV HOME /home/connectal
ENV CONNECTALDIR /usr/share/connectal
VOLUME /home/connectal/work
WORKDIR /home/connectal/work

RUN cp -r /usr/share/connectal/examples/simple /home/connectal
RUN chown -R connectal.users /home/connectal
