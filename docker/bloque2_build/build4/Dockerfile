FROM alpine:3.19.0

ADD http://www.vlsitechnology.org/pharosc_8.4.tar.gz /test/
COPY pharosc_8.4.tar.gz /test2/
ADD pharosc_8.4.tar.gz /test3/
ADD myfile.txt /tmp/myfile.txt
COPY myfile.txt /tmp2/

RUN ls -la /test/
RUN ls -la /test2/
RUN ls -la /test3/
RUN ls -la /tmp/
RUN ls -la /tmp2/

CMD ["echo", "Hello world!"]