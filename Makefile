
all:
	#make -C centos7-dev-tools build
	make -C centos7-xbsv build
	make -C centos7-xbsv-worker build

tools:
	make -C tools build
