
## format:
##  -v hostdir:containerdir:ro
## In our environment, /scratch/bluespec contains all the bluespec installations
## The image is expecting to find /scratch/bluespec/Bluespec-2014.07.A
DOCKER_VOLUMES=-v /scratch/bluespec:/scratch/bluespec:ro
DOCKER_ENV=-e "LM_LICENSE_FILE=$(LM_LICENSE_FILE)"

run:
	#sudo docker run $(DOCKER_VOLUMES) -u xbsv $(USER):centos6 yum grouplist
	sudo docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -u xbsv $(USER):centos6 make -C /scratch/xbsv/examples/simple gen.bluesim build.bluesim run.bluesim

build:
	sudo docker build -t $(USER):centos6 .

clean:
	sudo docker rm `sudo docker ps -qa`
	sudo docker rmi `sudo docker images -f dangling=true`
