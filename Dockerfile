FROM debian

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install vim nano -y

ENTRYPOINT sh