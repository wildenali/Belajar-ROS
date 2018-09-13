#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    global g_range_ahead
    g_range_ahead = min(msg.ranges)

g_range_ahead = 1       # anything to start

scan_pub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
rospy.init_node('wander')
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    twist = Twist()
    if(g_range_ahead < 1):
        twist.linear.x = 0
    else:
        twist.linear.x = 0.1
    cmd_vel_pub.publish(twist)

    rate.sleep()
