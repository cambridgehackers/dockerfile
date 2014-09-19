
## format:
##  -v hostdir:containerdir:ro
## In our environment, /scratch/bluespec contains all the bluespec installations
## The image is expecting to find /scratch/bluespec/Bluespec-2014.07.A
DOCKER_VOLUMES=-v /scratch/bluespec:/scratch/bluespec:ro -v /scratch/Xilinx:/scratch/Xilinx:ro -v /scratch/android-ndk-r9d:/scratch/android-ndk-r9d:ro
DOCKER_ENV=-e LM_LICENSE_FILE=$(LM_LICENSE_FILE)

run:
	#sudo docker run $(DOCKER_VOLUMES) $(USER):centos6-xbsv easy_install ply
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u xbsv $(USER):centos6-xbsv make V=1 -C /scratch/xbsv/examples/simple gen.bluesim build.bluesim run.bluesim
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u xbsv $(USER):centos6-xbsv which vivado
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u xbsv $(USER):centos6-xbsv make V=1 -C /scratch/xbsv/examples/simple gen.zedboard build.zedboard run.zedboard


build:
	sudo docker build -t $(USER):centos6-xbsv .

clean:
	docker rm `docker ps -qa` || true
	docker rmi `docker images -f dangling=true -qa` || true
