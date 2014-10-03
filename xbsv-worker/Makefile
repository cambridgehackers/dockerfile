
build: buildbot-xbsv-config.tar.gz
	sudo docker build --no-cache -t centos7-worker .

buildbot-xbsv-config.tar.gz:
	git clone /lab/asic/buildbot-xbsv-config.git buildbot-xbsv-config
	tar -zcvf buildbot-xbsv-config.tar.gz buildbot-xbsv-config
