# build

## Arg and Env in dockerfiles



docker build .
docker build --progress plain .
docker build --no-cache --progress plain .
docker image ls -a

docker build --no-cache --progress plain -t test .

docker run -it --rm test /bin/sh

=> Check if variables MY_ENV_VAR and MY_TEST_VAR are defined


docker build --no-cache --build-arg MY_BUILD_VAR=TEST2 -t test --progress plain .

let's try again docker run 
docker run -it --rm test /bin/sh
env var can be changed at runtime
docker run -it --rm -e MY_ENV_VAR=OTHER test /bin/sh


docker build --no-cache --progress plain -t test2 -f d2.Dockerfile .
docker build --no-cache --progress plain --build-arg MY_BUILD_VAR=TEST2 -t test2 -f d2.Dockerfile .