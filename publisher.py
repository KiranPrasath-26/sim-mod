#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
if __name__ == '__main__':
        rospy.init_node('publisher_node')
        pub = rospy.Publisher("/robot_publisher_node",String, queue_size=10)
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
                msg = String()
                msg.data = "hello, world!"
                rospy.loginfo("message published:")
                rospy.loginfo(msg.data)
                pub.publish(msg)
                rate.sleep()
        rospy.loginfo("Publisher Node stopped")
