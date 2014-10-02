# XBSV
# version 0.1

From vivado:2014.1
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN useradd -g users xbsv
ADD Bluespec-2014.07.A.tar.gz /scratch/bluespec/
ADD xbsv.repo /etc/yum.repos.d/xbsv.repo
RUN yum -y install xbsv
ADD flexlmrc /home/xbsv/.flexlmrc
ADD Xilinx.lic /home/xbsv/.Xilinx/Xilinx.lic
RUN chown -R xbsv.users /home/xbsv
RUN ln -s /usr/lib64/libgmp.so.10.1.1 /usr/lib64/libgmp.so.3
ENV BLUESPECDIR /scratch/bluespec/Bluespec-2014.07.A/lib
ENV PATH $PATH:/scratch/bluespec/Bluespec-2014.07.A/bin:/scratch/android-ndk-r9d:/scratch/Xilinx/Vivado/2014.1/bin
ENV HOME /home/xbsv
VOLUME /home/xbsv/work
WORKDIR /home/xbsv/work
