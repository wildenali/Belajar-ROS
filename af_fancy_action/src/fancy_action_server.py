#!/usr/bin/env python

import rospy
import time
import actionlib    # import ini untuk menggunakan SimpleActionServer class
from af_fancy_action.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback       # import TimerAction TimerGoal dan TimerResult di folder af_fancy_action

def do_timer(goal):     # fungsi program timer, ngpain sih fungsi ini, ini buat ngitung berapa lama waktu ketika si server menerima pesan goal yang di kirim oleh client
    start_time = time.time()
    update_count = 0

    if goal.time_to_wait.to_sec() > 60.0:   # jika lebih dari 60 detik, maka di aborted aja, karena terlalu lama
        result = TimerResult()
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)     # ini nih ngitung berapa lamanya
        result.updates_sent = update_count
        server.set_aborted(result, "timer aborted due to too-long wait")
        return

    while (time.time() - start_time) < goal.time_to_wait.to_sec():
        if server.is_preempt_requested():   # fungsi ini akan mengembalikan nilai TRUE, jika si client meminta memberhentikan mengejar goal
            result = TimerResult()
            result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
            result.updates_sent = update_count
            server.set_preempted(result, "Timer preempted")
            return

        feedback = TimerFeedback()      # mengirim feedback menggunakan TimerFeedback
        feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed
        server.publish_feedback(feedback)
        update_count += 1

        time.sleep(1.0)

    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = update_count
    server.set_succeeded(result, "Time completed successfully")

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()
