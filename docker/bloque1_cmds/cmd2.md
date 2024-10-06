# Run docker images

> PPT slides 41-48

## Simple run

docker run hello-world

=> Check how to build you own hello world container in docker/build/build1/


## Run a interactive container

docker run --name test -it alpine:3.7
Execute "exit" to exit.


## Run a container with different options

Go to bloque build and build3_python and build the container.

docker build -t mypythonapp .
docker run --name mypythoncontainer -p 8080:8080 mypythonapp
docker run -d --name mypythoncontainer2 -p 8080:8080 mypythonapp
docker run -d --name mypythoncontainer3 -p 8081:8080 -e MYENV:MYTESTVALUE mypythonapp

=> Check running containers with docker ps
=> Stop and delete all containers:

docker container ls -a --filter=name='mypythoncontainer.*'
docker container stop ...
docker container rm ...

## Stop, start, pause, unpause

docker run -d --name mypython0 -p 8080:8080 mypythonapp
docker run -d --name mypython1 -p 8081:8080 mypythonapp
=> Check that they are running
docker stop mypython0
docker pause mypython1
=> mypython1 is still in your "running" processes
docker unpause mypython1
docker start mypython0
=> Container "1" maintains RAM values while container 0 not.


## Commit

docker run --rm -d --name mypython0 -p 8080:8080 mypythonapp   (--rm removes container when stopped!!)
docker commit mypython0 mypythonapp_mod
docker image ls --filter=reference='mypython*'

docker run --rm -d --name mypython1 -p 8081:8080 mypythonapp_mod
docker ps to check


## Exec

docker exec -it mypython1 /bin/bash


## Inspect

docker inspect mypython1