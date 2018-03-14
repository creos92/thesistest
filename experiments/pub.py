#!/usr/bin/env python
import random
import time
import string
import rospy
from speedtest.msg import Datats
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', Datats, queue_size=0)
    rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(2000) # 10hz
    msg=Datats()
    print "invio dati"
    time.sleep(2)
    for i in range(0,501):
        msg.data= ''.join(['.' for x in range(i)])
        for y in range(0,11):
            msg.ts = rospy.Time.now()
            #print msg.ts
            pub.publish(msg)
        #rate.sleep()
    msg.data="0"
    print "termine invio dati\n"
    pub.publish(msg)
    time.sleep(5)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
