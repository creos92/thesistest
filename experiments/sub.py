#!/usr/bin/env python
import rospy
import random
import time
import string
from speedtest.msg import Datats
from std_msgs.msg import String
f=open('data.dat','w')

def callback(data):
    msg=[]
    now = rospy.get_rostime()
    msg.append(str(len(data.data)))
    msg.append("{}.{}".format(data.ts.secs, data.ts.nsecs))
    msg.append("{}.{}".format(now.secs, now.nsecs))
    f.write(", " .join(msg)+"\n")
    #f.write(", ".join(msg) + "\n")

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Datats, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    f.close()
