Da linea di comando:
Lato server:
su root 
svn checkout https://github.com/creos92/thesistest.git/trunk/DockerfileServer
docker build DockerfileServer/ -t parloma:servertest
docker-compose up

Lato Client:
su root
svn checkout https://github.com/creos92/thesistest.git/trunk/DockerfileClient
docker build DockerfileClient/ -t parloma:clienttest
docker-compose run -e IP=192.168.0.107 parloma_clienttest 


Altro:
Download del file
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
%ip link delete tun* %eliminare tutte le interfacce tun (tun0,tun1)
run -it --privileged --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -p 1194:1194 --name parloma_server parloma:server
docker run -it --privileged --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --name parloma_client parloma:client
export IP=$IP
xhost +local:root 
