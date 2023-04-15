#!/usr/bin/env python3
import pyautogui as pg
import rospy
from geometry_msgs.msg import Twist
from math import radians

def cursor_turtle():
        
        rospy.init_node('turtlesim1', anonymous=False) 
        
        pub = rospy.Publisher('turtle1/cmd_vel/', Twist, queue_size=10)
        r = rospy.Rate(10)

        forw = Twist()
        forw.linear.x = 0.2

        reve = Twist()
        reve.linear.x = -0.2

        lturn = Twist()
        lturn.linear.x = 0
        lturn.angular.z = radians(45) 

        rturn = Twist()
        rturn.linear.x = 0
        rturn.angular.z =  -radians(45)

        rospy.loginfo(radians(45))

        while not rospy.is_shutdown():
            x, y = pg.position()
            
            
            if(x < 1400 and x > 500 and y > 0 and y < 250):
                 rospy.loginfo("Forward")
                 pub.publish(forw)
                 r.sleep

            
            if(x < 1919 and x > 1550 and y > 350 and y < 800):
                 rospy.loginfo("Right Turning")
                 pub.publish(rturn)
                 r.sleep
            
            
            if(x < 400 and x > 0 and y > 350 and y < 800):
                 rospy.loginfo("left Turning")
                 pub.publish(lturn)
                 r.sleep

            if(x < 1400 and x > 500 and y > 900 and y < 1079):
                 rospy.loginfo("Backward")
                 pub.publish(reve)
                 r.sleep
            
 
if __name__ == '__main__':
    try:
        cursor_turtle()
    except:
        rospy.loginfo("node terminated.")