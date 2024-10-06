# ADD vs COPY

docker build --no-cache --progress plain .


Main differences
* ADD extracts local compressed file
* ADD works with external URLs
* COPY does not

# COPY example

docker build --progress plain -t test2 -f d2.Dockerfile .

docker run -p 8090:80 test2
Go to http://localhost:8090/