#!/usr/bin/python3
import rclpy
import sys
from rclpy import qos
from geometry_msgs.msg import Twist

def draw_circle():
    global pub_vel
    msg = Twist()
    msg.linear.x = 3.0
    msg.angular.z = 5.0   
    pub_vel.publish(msg)

def main(args=None):
    rclpy.init(args=sys.argv)
    global pub_vel
    node = rclpy.create_node("Circle")
    pub_vel = node.create_publisher(Twist,"turtle1/cmd_vel",qos_profile=qos.qos_profile_parameters)
    node.get_logger().info("Circle started")
    timer = node.create_timer(0.1,draw_circle)
    try:
        rclpy.spin(node)  # Spin only one node to handle callbacks
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
    
if __name__=="__main__":
    main()
