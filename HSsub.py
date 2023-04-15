#!/usr/bin/env python3
import rospy
from ros_lab_msgs.msg import HardwareStatus
def callback_data(msg):
        rospy.loginfo("Message received:")
        rospy.loginfo(msg)


if __name__ == '__main__':
        rospy.init_node('subscriber')
        sub = rospy.Subscriber("/hwstatus_node", HardwareStatus, callback_data)
        rospy.spin()
