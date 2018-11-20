#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy


def joy_cb(data):
    pub_head = rospy.Publisher('/cmd_joints', JointState)
    
    servo_command = JointState()
    servo_command.name = ['head_pan_joint', 'head_tilt_joint']
    servo_command.position = [data.axes[3], data.axes[4]]

    pub_head.publish(servo_command)
    

def main():
    rospy.init_node('qbo_joy_control')

    rospy.Subscriber('/joy', Joy, joy_cb)
    rospy.spin()


if __name__ == "__main__":
    while not rospy.is_shutdown:
        main()






