#!/bin/bash
source ./devel/setup.bash
chmod +rx /Server/certificati/server/start_server.sh &&
cd /Server/certificati/server && sync && ./start_server.sh &
sleep 1s
roscore &
sleep 2s
export ROS_IP=10.8.0.1
export ROS_MASTER_URI=http://10.8.0.1:11311
ntpdate ntp.ubuntu.com && 
cd /experiments && source ./devel/setup.bash && python sub.py && cp data.dat ../data && cat data.dat
