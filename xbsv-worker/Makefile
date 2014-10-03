
build: buildbot-xbsv-config.tar.gz id_rsa id_rsa.pub
	sudo docker build --no-cache -t centos7-worker .

id_rsa id_rsa.pub:
	sudo cp -a /scratch/buildbot/id_rsa* .

buildbot-xbsv-config.tar.gz:
	git clone /lab/asic/buildbot-xbsv-config.git buildbot-xbsv-config
	tar -zcvf buildbot-xbsv-config.tar.gz buildbot-xbsv-config
