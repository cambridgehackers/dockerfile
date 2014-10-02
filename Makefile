
all:
	make -C centos7-dev-tools build
	make -C android-ndk-r9d build
	make -C vivado build
	make -C centos7-xbsv build
	make -C centos7-xbsv-worker build
