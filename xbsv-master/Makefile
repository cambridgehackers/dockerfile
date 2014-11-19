
run:
	docker run -i -t -p 8080:8080 -p 9989:9989 -e HOME=/scratch/buildbot --dns=10.0.0.61 jameyhicks/buildbot-master sh

build: id_rsa id_rsa.pub buildbot-xbsv-config.tar.gz
	sudo docker build --no-cache -t centos7-master .

id_rsa id_rsa.pub:
	sudo cp -a /scratch/buildbot/id_rsa* .

buildbot-xbsv-config.tar.gz:
	git clone /lab/asic/buildbot-xbsv-config.git buildbot-xbsv-config
	tar -zcvf buildbot-xbsv-config.tar.gz buildbot-xbsv-config
