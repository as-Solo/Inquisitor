docker network create --driver bridge red_LAN
docker build -t inquisitor .
docker run -dit --rm --name victima1 --mount type=bind,src=/home/solo/Desktop/solo/42/cyber/Inquisitor/victimas,dst=/victima1 --network red_LAN alpine sh
docker run -dit --rm --name victima2 --mount type=bind,src=/home/solo/Desktop/solo/42/cyber/Inquisitor/victimas,dst=/victima2 --network red_LAN alpine sh
docker run -dit --rm --name atacante --mount type=bind,src=/home/solo/Desktop/solo/42/cyber/Inquisitor/atacante,dst=/atacante --network red_LAN inquisitor sh