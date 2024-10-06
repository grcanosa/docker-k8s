# Common commands

> Check PPT 37-40

Run a container:

docker run hello-world



## Pull


docker pull alpine:3.19.0


## Images

docker images -a

## Push

Go to hub.docker.com and create an account.

try to push an image:

docker tag alpine:3.19.0 grcanosa/alpine:3.19.0
docker push grcanosa/alpine:3.19.0

=> You need to login first

docker login  
docker login registry-1.docker.io

=> Retry: docker push grcanosa/alpine:3.19.0

## Tag

to "rename" a docker image to a new name or tag.





