#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import radians

def turtle_square():
        rospy.init_node('turtlesim1', anonymous=False) 
        
        pub = rospy.Publisher('turtle1/cmd_vel/', Twist, queue_size=10)
        r = rospy.Rate(10)

        forw = Twist()
        forw.linear.x = 0.2

        turn = Twist()
        turn.linear.x = 0
        turn.angular.z = radians(45) 
        rospy.loginfo(radians(45))
        count = 0
        while not rospy.is_shutdown():
            rospy.loginfo("Going Straight")
            for x in range(0,50):
                pub.publish(forw)
                r.sleep()
            rospy.loginfo("Turning")
            for x in range(0,20):
                pub.publish(turn)
                r.sleep()            
            count = count + 1
            if(count == 4): 
                    count = 0
            if(count == 0): 
                    rospy.loginfo("TurtleBot should be close to the original starting position (but it's probably way off)")
 
if __name__ == '__main__':
    try:
        turtle_square()
    except:
        rospy.loginfo("node terminated.")