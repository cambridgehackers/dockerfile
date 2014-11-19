

build: Dockerfile android-ndk-r9d.tar.gz
	docker build -t android-ndk:r9d .

android-ndk-r9d.tar.gz: /scratch/android-ndk-r9d
	tar -zcvf android-ndk-r9d.tar.gz -C /scratch/ android-ndk-r9d

