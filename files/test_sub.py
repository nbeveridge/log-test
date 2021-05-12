#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int64
from std_msgs.msg import String
import sys
import time

def callback(msg):
    heard = msg.data
    rospy.loginfo('heard topic ' + heard)
    orig_stdout = sys.stdout
    rospy.loginfo('orig_stdout = '+str(orig_stdout))
    path = 'C:\\Users\\neilb\\desktop\\text.txt'
    sys.stdout = open(path, 'w')
    time.sleep(1)
    new_stdout = sys.stdout
    rospy.loginfo('new_stdout = '+str(new_stdout))
    print('iuedjvnkj')
    sys.stdout.close()
    sys.stdout=orig_stdout 

rospy.init_node('test_sub')  

rospy.Subscriber('test', String, callback,queue_size=1)

rospy.spin()

# print(7)
# import sys
# import time
# orig_stdout = sys.stdout
# path = 'C:\\Users\\neilb\\desktop\\text.txt'
# # sys.stdout.write('123')# = open(path, 'w')
# sys.stdout = open(path, 'w')
# time.sleep(1)
# print('ekfcn')
# sys.stdout.close()
# sys.stdout=orig_stdout 

maybe make the log file in the docker container
then open another terminal and use the below 
method to copy over the file when you want to see it


In order to copy a file from a running container to your host you first need to get your Docker container ID, you can do that with the following command:

docker ps
 
 
Then once you have your container ID, you can run the following:

docker cp container_id:/path/to/your_file.txt /path/on/your/host