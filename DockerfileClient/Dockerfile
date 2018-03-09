FROM osrf/ros:indigo-desktop-full
RUN      \
        svn checkout https://github.com/creos92/thesis.git/trunk/Client &&\
	svn checkout https://github.com/creos92/thesis.git/trunk/experiments &&\
        apt-get update && apt-get install build-essential libssl-dev liblzo2-dev libpam0g-dev  wget -y && \
        wget https://swupdate.openvpn.org/community/releases/openvpn-2.4.4.tar.gz && sudo tar zxvf openvpn-2.4.4.tar.gz && cd openvpn-2.4.4 && ./configure && make && checkinstall -y && \
        /bin/bash -c "cd /experiments && catkin_make"

CMD cd experiments && chmod +rx start_c.sh && sync && ./start_c.sh
