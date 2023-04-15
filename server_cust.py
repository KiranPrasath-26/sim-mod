#!/usr/bin/env python3

import rospy
from ros_lab.srv import MulTwoFloat

def handle_mul_two_floats(req):
    result = req.a * req.b
    rospy.loginfo("Product of " +str(req.a)+ " and " +str(req.b) + " is " + str(result))
    return result

if __name__ == '__main__':
    rospy.init_node("mul_two_floats_server")
    rospy.loginfo("Multiply two float server node created")
    service = rospy.Service("/mul_two_float", MulTwoFloat, handle_mul_two_floats)
    rospy.loginfo("Service server has been started")
    rospy.spin()