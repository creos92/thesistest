#!/usr/bin/env python
import rospy
import random
import time
import string
from speedtest.msg import Datats
from std_msgs.msg import String

def callback(data):
    msg=[]
    now = rospy.Time.now()
    msg.append(str(len(data.data)))
    msg.append("{}.{}".format(data.ts.secs, data.ts.nsecs))
    msg.append("{}.{}".format(now.secs, now.nsecs))
    if (data.data != "0"):
        mem.append(str(", " .join(msg)+"\n"))
    else:
	f=open('data.dat','w')
	for dato in mem:
		f.write(dato)
	print ("Dati caricati su data.dat")
        f.close()
        rospy.signal_shutdown("finish")

def listener():
    global mem
    mem=[]
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Datats, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
