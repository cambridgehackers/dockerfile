

dockerimage: Dockerfile android-ndk-r9d.tar.gz
	sudo docker build -t android-ndk:r9d .
	sudo docker tag android-ndk:r9d localhost:5000/android-ndk-r9d

android-ndk-r9d.tar.gz: /scratch/android-ndk-r9d
	tar -zcvf android-ndk-r9d.tar.gz -C /scratch/ android-ndk-r9d

