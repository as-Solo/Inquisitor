#! /bin/sh

yes | docker network prune && docker network create --driver bridge inquisitor_lan
docker build -t atacante atacante/
docker build -t victimas victimas/