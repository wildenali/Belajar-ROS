#!/usr/bin/env python

import rospy
import time
import actionlib    # import ini untuk menggunakan SimpleActionServer class
from ae_action.msg import TimerAction, TimerGoal, TimerResult       # import TimerAction TimerGoal dan TimerResult di folder ae_action

def do_timer(goal):     # fungsi program timer, ngpain sih fungsi ini, ini buat ngitung berapa lama waktu ketika si server menerima pesan goal yang di kirim oleh client
    start_time = time.time()
    time.sleep(goal.time_to_wait.to_sec())
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)     # ini nih ngitung berapa lamanya
    result.updates_sent = 0
    server.set_succeeded(result)

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()
