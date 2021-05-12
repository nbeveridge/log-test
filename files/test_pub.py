#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
from std_msgs.msg import Bool
import time


rospy.init_node('test_pub')

pub = rospy.Publisher('test', String, queue_size=1)

while(True):
    pub.publish('test')
    time.sleep(1)