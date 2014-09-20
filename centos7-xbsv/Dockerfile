# XBSV
# version 0.1

From jamey:centos7-dev-tools
Maintainer Jamey Hicks <jamey.hicks@qrclab.com>
RUN useradd -g users xbsv
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
WORKDIR /scratch/xbsv
ADD flexlmrc /home/xbsv/.flexlmrc
ADD Xilinx.lic /home/xbsv/.Xilinx/Xilinx.lic
RUN chown -R xbsv.users /scratch/xbsv /home/xbsv

RUN ln -s /usr/lib64/libgmp.so.10.1.1 /usr/lib64/libgmp.so.3
ENV BLUESPECDIR /scratch/bluespec/Bluespec-2014.07.A/lib
ENV PATH $PATH:/scratch/bluespec/Bluespec-2014.07.A/bin:/scratch/android-ndk-r9d:/scratch/Xilinx/Vivado/2014.1/bin
USER xbsv
ENV HOME /home/xbsv
VOLUME /home/xbsv/work
WORKDIR /home/xbsv/work
