#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import sys
import rclpy
from rclpy import qos
from std_msgs.msg import String
import time    

def main(args=None):
    rclpy.init(args=sys.argv)
    nodes = []    
    node = rclpy.create_node("talker")
    pub1 = node.create_publisher(String, "talker_1", qos_profile=qos.qos_profile_parameters)
    pub2 = node.create_publisher(String, "talker_2", qos_profile=qos.qos_profile_parameters)
    pub3 = node.create_publisher(String, "talker_3", qos_profile=qos.qos_profile_parameters)
    counter = 1
    id = 1

    while(1):
        msg = String()
        msg.data = "Hello from SRA %d" %counter
        if id==1:
            pub1.publish(msg)
        elif id == 2:
            pub2.publish(msg)
        elif id == 3:
            pub3.publish(msg)           
                
        node.get_logger().info('Publishing: "%s"' % msg.data)
        count += 1
        if count > 50:
            count = 1
            id += 1
            if id > 3:
                id = 1
        
        time.sleep(0.1)  
        nodes.append(node)
    
    try:
        rclpy.spin(nodes[0])  # Spin only one node to handle callbacks
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__ == "__main__":
    main()



    

