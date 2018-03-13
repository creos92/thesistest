#!/usr/bin/env python
import random
import time
import string
import rospy
from speedtest.msg import Datats
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', Datats, queue_size=5000)
    rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    msg=Datats()
    for i in range(0,500):
        msg.data= ''.join(['.' for x in range(i)])
        for y in range(0,11):
            msg.ts = rospy.get_rostime()
            pub.publish(msg)
        rospy.sleep(0.05)
    msg.data="0"
    print "pubblico uno 0\n"
    pub.publish(msg)
    time.sleep(30)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

