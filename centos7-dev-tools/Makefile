
## format:
##  -v hostdir:containerdir:ro
DOCKER_VOLUMES=
DOCKER_ENV=

shell:
	docker run $(DOCKER_ENV) $(DOCKER_VOLUMES) -i -t centos7-dev-tools /bin/sh

build:
	docker build -t centos7-dev-tools:latest .

clean:
	docker rm `docker ps -qa` || true
	docker rmi `docker images -f dangling=true -qa` || true
