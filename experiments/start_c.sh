#!/bin/bash
source ./devel/setup.bash
sed -i "s/indirizzoipserver/"$IP"/g" ../Client/certificati/client1/client.conf
chmod +rx /Client/certificati/client1/start_client.sh &&
cd /Client/certificati/client1 && sync && ./start_client.sh &
sleep 15s
export ROS_IP=$(/sbin/ifconfig | grep "inet addr:10.8" |awk -F: '{print $2}' | awk '{print $1}')
export ROS_MASTER_URI=http://10.8.0.1:11311
ntpdate ntp.ubuntu.com && 
cd /experiments && python pub.py
