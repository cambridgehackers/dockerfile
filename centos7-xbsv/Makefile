
## format:
##  -v hostdir:containerdir:ro
## In our environment, /scratch/bluespec contains all the bluespec installations
## The image is expecting to find /scratch/bluespec/Bluespec-2014.07.A
WORK=$(HOME)
DOCKER_VOLUMES=-v /scratch/bluespec:/scratch/bluespec:ro -v /scratch/Xilinx:/scratch/Xilinx:ro -v /scratch/android-ndk-r9d:/scratch/android-ndk-r9d:ro -v $(WORK):$(WORK):rw

DOCKER_ENV=-e LM_LICENSE_FILE=$(LM_LICENSE_FILE) -e DISPLAY=$(DISPLAY)

shell:
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u xbsv -i -t $(USER):centos7-xbsv /bin/sh

root:
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u root -i -t $(USER):centos7-xbsv /bin/sh

run:
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u xbsv $(USER):centos7-xbsv make V=1 -C /scratch/xbsv/examples/simple gen.bluesim build.bluesim run.bluesim
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u xbsv $(USER):centos7-xbsv make V=1 -C /scratch/xbsv/examples/simple gen.zedboard build.zedboard run.zedboard


build:
	cp ~/.Xilinx/Xilinx.lic .
	cp ~/.flexlmrc flexlmrc || touch flexlmrc
	#sudo docker build --no-cache=true -t centos7-xbsv .
	sudo docker build -t centos7-xbsv .

clean:
	docker rm `docker ps -qa` || true
	docker rmi `docker images -f dangling=true -qa` || true
