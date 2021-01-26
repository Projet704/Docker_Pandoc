FROM alpine:latest 

RUN apk add python3 py3-pip --no-cache \
&& wget https://dl-cdn.alpinelinux.org/alpine/edge/testing/x86_64/pandoc-2.9.2.1-r0.apk \
&& tar -zxvf pandoc-2.9.2.1-r0.apk \ 
&& apk add git
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "./test.py","url.json"] 
