#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def callback_data(msg):
        rospy.loginfo("Message received:")
        rospy.loginfo(msg.data)


if __name__ == '__main__':
        rospy.init_node('subscriber')
        sub = rospy.Subscriber("/robot_publisher_node", String, callback_data)
        rospy.spin()
