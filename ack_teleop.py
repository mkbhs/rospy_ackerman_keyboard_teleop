import rospy
import time
import sys
import numpy as np

from getch import getch
from math import *
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float64

min_steering = -0.2
max_steering = 0.2
step_steering = 0.05

min_vel = -5
max_vel = 20
step_vel = 1

def updateCommand(key, current_steering, current_vel):

    next_steering = current_steering
    next_vel = current_vel

    if(key=='a')or(key=='A'):
        if(current_steering > min_steering):
            next_steering = current_steering - step_steering

    elif(key=='d')or(key=='D'):
        if(current_steering < max_steering):
            next_steering = current_steering + step_steering

    elif(key=='w')or(key=='W'):
        if(current_vel < max_vel):
            next_vel = current_vel + 1

    elif(key=='s')or(key=='S'):
        if(current_vel > min_vel):
            next_vel = current_vel - 1

    return next_steering, next_vel


rospy.init_node('ack_teleop', anonymous=False)
steering_pub = rospy.Publisher('/steering_cmd', Float64, queue_size=1)
vel_pub = rospy.Publisher('/vel_cmd', Float64, queue_size=1)
loop_rate = rospy.Rate(10)

steering = 0.0
vel = 0.0

while not rospy.is_shutdown():
    key = getch()
    steering, vel = updateCommand(key, steering, vel)
    print("steering = " + str(steering) + "\t\t" + "vel = " + str(vel))
    steering_pub.publish(steering)
    vel_pub.publish(vel)
    loop_rate.sleep()
