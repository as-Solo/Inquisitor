FROM debian:stable

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install vsftpd -y
RUN apt-get install net-tools -y

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 20 21

ENTRYPOINT ["/docker-entrypoint.sh"]