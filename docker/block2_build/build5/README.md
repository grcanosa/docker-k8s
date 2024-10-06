# EntryPoint and CMD


docker build -t test .
docker run test

> CMD is an "argument" of ENTRYPOINT.

Exercise: Change the Dockerfile to make it say "Hello YOUR_NAME" but YOUR_NAME can be provided in each execution (each docker run). Tip: Change entrypoint for CMD.

