

dockerimage: Dockerfile vivado-2014.1.tar.gz
	sudo docker build -t vivado:2014.1 .
	sudo docker tag vivado:2014.1 localhost:5000/vivado-2014.1

vivado-2014.1.tar.gz: /scratch/Xilinx/Vivado/2014.1
	tar -zcvf vivado-2014.1.tar.gz -C /scratch/Xilinx/Vivado 2014.1

