
MASTERNAME?=sj9

build:
	hostname > workername.txt
	echo $(MASTERNAME) > mastername.txt
	cp -a /scratch/buildbot/.ssh/id_rsa .
	docker build --no-cache -t centos7-worker .
	rm -f id_rsa

buildbot-xbsv-config.tar.gz:
	git clone /lab/asic/buildbot-xbsv-config.git buildbot-xbsv-config
	tar -zcvf buildbot-xbsv-config.tar.gz buildbot-xbsv-config
