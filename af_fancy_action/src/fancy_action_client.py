#!/usr/bin/env python
import rospy
import time
import actionlib        # import ini untuk menggunakan SimpleActionServer class
from af_fancy_action.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback       # import TimerAction TimerGoal dan TimerResult di folder af_fancy_action

def feedback_cb(feedback):
    print('[feedback] Time elapsed: %f'%(feedback.time_elapsed.to_sec()))
    print('[feedback] Time remaining: %f'%(feedback.time_remaining.to_sec()))


rospy.init_node('timer_action_client')      # menamai node
client = actionlib.SimpleActionClient('timer', TimerAction)     # menghubungkan dengan server dengan nama 'timer'
client.wait_for_server()        # tunggu konek ke server
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)    # seting waktu berapa lama waktu yang di tunngu si client, yg akan di kirim ke server
client.send_goal(goal, feedback_cb=feedback_cb)      # kirim data ke server

client.wait_for_result()    # tunggu hasilnya
print('[Result] State: %d'%(client.get_state()))
print('[Result] Status: %s'%(client.get_goal_status_text()))
print('[Result] Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))
print('[Result] Updates sent: %d'%(client.get_result().updates_sent))
