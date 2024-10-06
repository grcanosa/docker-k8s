# Using "bind" directories as volumes

We can also "bind" a local volume


docker run --name my-nginx -v ./nginx-data/:/usr/share/nginx/html/ -p 8080:80 nginx


> Repeat tests of previous example with this type of volume.
