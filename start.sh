#! /bin/sh

TAG=ds4se

if [ $# -eq 1 ]; then
	if [ "$1" = "--build" ]; then
		# Build the docker container
		docker build -t $TAG .
	fi
fi


# Run the docker container. Add additional -v if
# you need to mount more volumes into the container
# Also, make sure to edit the ports to fix your needs.
docker run -d --runtime=nvidia -v $(pwd):/tf/main \
	-v /mnt/data/ds4se:/tf/data \
	-p 8004:8888  $TAG
