#!/usr/bin/env python

import rospy
from ad_service.srv import WordCount
import sys

rospy.init_node('service_client')   # nama node service nya
rospy.wait_for_service('word_count')    # tunggu service yang di jalankan oleh server
word_counter = rospy.ServiceProxy('word_count', WordCount)  # kalau si client di jalankan, tanpa si server duluan, maka nanti akan gagal programmnya

words = ' '.join(sys.argv[1:])
word_count = word_counter(words)    # spesifik nama dari service
print words, '->', word_count.count
