# Export


## Save / Export

docker save -o myapp.tar mypythonapp   => Save docker image into a .tar file

docker export -o mycontainer.tar mypython0 => Save docker container into a .tar file


## Import

docker image rm mypythonapp
docker image rm mypythonapp_mod

docker import mycontainer.tar mypythonapp_reimported
docker load -i myapp.tar

docker image ls -a | grep mypythonapp

