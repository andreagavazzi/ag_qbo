#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState


def say_no():
    pub_head = rospy.Publisher('/cmd_joints', JointState, queue_size=1)

    servo_command = JointState()
    servo_command.name = ['head_pan_joint']
    servo_command.position = [0.80]

    pub_head.publish(servo_command)


if __name__ == '__main__':
    rospy.init_node('qbo_mimic')
    while not rospy.is_shutdown()
    say_no()
rospy.spin()