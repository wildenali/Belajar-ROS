#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('mixing')

def callback(msg):
    mixing = Int32()
    mixing.data = msg.data * 2
    pub.publish(mixing)

sub = rospy.Subscriber('number', Int32, callback)
pub = rospy.Publisher('mixing', Int32, queue_size = 1)

rospy.spin()
