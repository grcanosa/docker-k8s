# Using docker volumes

docker volume create my-vol-nginx

docker run --name my-nginx -v my-vol-nginx:/usr/share/nginx/html/ -p 8080:80 nginx

Go to http://localhost:8080/ and to http://localhost:8080/prueba.html

docker exec -it my-nginx /bin/bash

cd /usr/share/nginx/html/
echo "My_test" > prueba.html


Exit container and remove it.

Launch it again:

docker run --name my-nginx -v my-vol-nginx:/usr/share/nginx/html/ -p 8080:80 nginx

Go to http://localhost:8080/ and to http://localhost:8080/prueba.html

You can even launch 2 containers using the same volume!

docker run --name my-nginx -v my-vol-nginx:/usr/share/nginx/html/ -p 8080:80 nginx
docker run --name my-nginx2 -v my-vol-nginx:/usr/share/nginx/html/ -p 8081:80 nginx
