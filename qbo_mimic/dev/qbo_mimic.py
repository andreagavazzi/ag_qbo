#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState


def say_yes():
    pass


def say_no():
    pub_head = rospy.Publisher('/cmd_joints', JointState)
    servo_command = JointState()
    servo_command.name = ['head_pan_joint']
    servo_command.position = [0.80]

    pub_head.publish(servo_command)


def smile():
    pass


def frown():
    pass


def kiss():
    pass


def calm():
    pass


def angry():
    pass


def main():
    rospy.init_node('qbo_mimic')
    rate = rospy.Rate(10)
    say_no()
    rate.sleep()
    #rospy.spin()

if __name__ == "__main__":
    main()