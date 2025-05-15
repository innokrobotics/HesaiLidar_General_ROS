#!/usr/bin/env python

import rospy
from std_srvs.srv import SetBool

def send_request(state):
    rospy.wait_for_service("sensor_status")
    try:
        service_proxy = rospy.ServiceProxy("sensor_status", SetBool)
        response = service_proxy(state)
        rospy.loginfo(f"Response: success={response.success}, {response.message}")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service erreur : {e}")

def main():
    rospy.init_node("sensor_status_client")
    while True:
        state_sensor = input("Enter 'True' to turn on lidar, 'False' otherwise: ").lower()
        if state_sensor in ["true", "false"]:
            state = state_sensor == "true"
            send_request(state)
            break
        else:
            rospy.logwarn("Invalid input. Please enter 'True' or 'False'.")

if __name__ == "__main__":
    main()

