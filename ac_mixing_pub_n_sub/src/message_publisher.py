#!/usr/bin/env python

import rospy

from ac_mixing_pub_n_sub.msg import Complex
from random import random   # library untuk manggil angka random

rospy.init_node('message_publisher')
pub = rospy.Publisher('complex', Complex, queue_size = 1)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    msg = Complex()
    msg.real = random()
    msg.imaginary = random()

    pub.publish(msg)
    rate.sleep()
