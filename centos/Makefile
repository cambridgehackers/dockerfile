
run:
	sudo docker run -v /scratch/bluespec:/scratch/bluespec:ro -u xbsv $(USER):centos6 make -C /scratch/xbsv/examples/simple gen.bluesim build.bluesim run.bluesim

build:
	sudo docker build -t $(USER):centos6 .

clean:
	sudo docker rm `sudo docker ps -qa`
	sudo docker rmi `sudo docker images -f dangling=true`
