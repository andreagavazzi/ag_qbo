#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState


def say_yes():
    pass


def say_no():
    pub_head = rospy.Publisher('/cmd_joints', JointState)
    servo_command = JointState()
    servo_command.name = ['head_pan_joint']
    servo_command.velocity = [2]

    servo_command.position = [1]
    pub_head.publish(servo_command)
    rospy.sleep(0.4)

    servo_command.position = [-1]
    pub_head.publish(servo_command)
    rospy.sleep(0.8)

    servo_command.position = [-1]
    pub_head.publish(servo_command)
    rospy.sleep(0.4)


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
    say_no()


if __name__ == '__main__':
    rospy.init_node('qbo_mimic')
    rospy.sleep(0.5)
    rospy.loginfo('Node qbo_mimic is now up')
    while not rospy.is_shutdown():
        main()

rospy.spin()
