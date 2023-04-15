#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
if __name__ == '__main__':
        rospy.init_node('publisher_node1')
        pub = rospy.Publisher("/robot_publisher_node1", Float32, queue_size=10)
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
                msg = Float32()
                msg.data = 20.04
                rospy.loginfo(msg)
                pub.publish(msg)
                rate.sleep()
        rospy.loginfo("Publisher Node stopped")
