#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int64
from std_msgs.msg import String

def callback(msg):
    heard = msg.data
    print('heard topic' + heard)

rospy.init_node('test_sub')  

rospy.Subscriber('test', Bool, callback,queue_size=1)
