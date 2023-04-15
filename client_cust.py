#!/usr/bin/env python3

import rospy
from ros_lab.srv import MulTwoFloat
if __name__ == '__main__':
    rospy.init_node("mul_two_float_client")
    rospy.wait_for_service("/mul_two_float")
    try:
        mul_two_float = rospy.ServiceProxy("/mul_two_float", MulTwoFloat)
        response = mul_two_float(2,6)
        rospy.loginfo("Product is :" +str(response.prod))
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed:" +str(e))