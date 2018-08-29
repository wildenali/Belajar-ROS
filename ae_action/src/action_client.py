#!/usr/bin/env python
import rospy
import actionlib        # import ini untuk menggunakan SimpleActionServer class
from ae_action.msg import TimerAction, TimerGoal, TimerResult       # import TimerAction TimerGoal dan TimerResult di folder ae_action

rospy.init_node('timer_action_client')      # menamai node
client = actionlib.SimpleActionClient('timer', TimerAction)     # menghubungkan dengan server dengan nama 'timer'
client.wait_for_server()        # tunggu konek ke server
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)    # seting waktu berapa lama waktu yang di tunngu si client, yg akan di kirim ke server
client.send_goal(goal)      # kirim data ke server
client.wait_for_result()    # tunggu hasilnya
print('Time elapsed: %f' % (client.get_result().time_elapsed.to_sec()))     # nah nampilin hasilnya
