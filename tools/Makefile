

build: Dockerfile android-ndk-r9d.tar.gz Bluespec-2014.05.beta1.tar.gz vivado-2014.1.tar.gz
	sudo docker build -t tools:latest .

android-ndk-r9d.tar.gz: /scratch/android-ndk-r9d
	tar -zcvf android-ndk-r9d.tar.gz -C /scratch/ android-ndk-r9d

Bluespec-2014.05.beta1.tar.gz: /scratch/bluespec/Bluespec-2014.05.beta1
	tar -zcvf Bluespec-2014.05.beta1.tar.gz -C /scratch/bluespec Bluespec-2014.05.beta1

