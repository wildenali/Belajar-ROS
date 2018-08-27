#!/usr/bin/env python

import rospy
from ad_service.srv import WordCount, WordCountResponse

def count_words(request):
    return WordCountResponse(len(request.words.split()))
    # or
    # return len(request.words.split())     # kalau single return arguments for the service
    # or
    # return [len(request.words.split())]   # ini kalau mutliple return argument, bisa pakai tuple atau list
    # or
    # return {'count': len(request.words.split())}      # ini kalau nge return dictionary

rospy.init_node('service_server')

service = rospy.Service('word_count', WordCount, count_words)

rospy.spin()
