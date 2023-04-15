#!/usr/bin/env python3
import rospy
from ros_lab_msgs.msg import HardwareStatus
if __name__ == '__main__':
        rospy.init_node('publisher_node')
        pub = rospy.Publisher("/hwstatus_node",HardwareStatus, queue_size=10)
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
                msg = HardwareStatus()
                msg.temperature = 60
                msg.are_motors_up = True
                msg.debug_message = "heki desu"
                rospy.loginfo("message published:")
                rospy.loginfo(msg)
                pub.publish(msg)
                rate.sleep()
        rospy.loginfo("Publisher Node stopped")