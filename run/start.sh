#! /bin/sh

docker rm -fv client && docker run --name client --mount type=bind,src=$(pwd)/victimas,dst=/client --network inquisitor_lan -dit victimas
docker rm -fv server && docker run --name server --mount type=bind,src=$(pwd)/victimas,dst=/server --network inquisitor_lan -dit victimas
docker rm -fv spoofer && docker run --name spoofer --mount type=bind,src=$(pwd)/atacante,dst=/spoofer --network inquisitor_lan -dit atacante
