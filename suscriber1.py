#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
def callback_data(msg):
        rospy.loginfo("Message received:")
        rospy.loginfo(msg)


if __name__ == '__main__':
        rospy.init_node('subscriber1')
        sub = rospy.Subscriber("/robot_publisher_node", String, callback_data)
        sub1 = rospy.Subscriber("/robot_publisher_node1", Float32, callback_data)
        rospy.spin()
