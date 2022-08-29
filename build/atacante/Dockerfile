FROM debian:stable

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install vim -y
RUN apt-get install python3 -y
RUN apt-get install net-tools -y

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 20 21

ENTRYPOINT ["/docker-entrypoint.sh"]