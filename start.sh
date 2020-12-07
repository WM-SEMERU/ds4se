#! /bin/sh

DATA=$1
PORT=$2
TAG=mlproj

if [ $# -eq 3 ]; then
	if [ "$3" = "--build" ]; then
		# Build the docker container
		docker build -t $TAG .build
	fi
fi


# Run the docker container. Add additional -v if
# you need to mount more volumes into the container
# Also, make sure to edit the ports to fix your needs.
docker run -d --gpus all -it -p $PORT:8888 -v $(pwd):/home/jovyan/work		\
	-v $DATA:/home/jovyan/data -e GRANT_SUDO=yes -e JUPYTER_ENABLE_LAB=yes	\
	--restart always --name $TAG $TAG