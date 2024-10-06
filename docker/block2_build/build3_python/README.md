# Python app


docker build -t mypythonapp .

To run it:

docker run --name mypythoncontainer -p 8080:8080 mypythonapp

Run it "detached"

docker run -d --name mypythoncontainer2 -p 8080:8080 mypythonapp