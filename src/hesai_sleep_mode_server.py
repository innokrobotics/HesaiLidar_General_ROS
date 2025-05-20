#!/usr/bin/env python

import rospy
import requests
from std_srvs.srv import SetBool, SetBoolResponse

def handle_sensor_status(req):
    rospy.loginfo(f"Request received: {req.data}")
    server_ip = rospy.get_param("server_ip", "192.168.1.201")
    if req.data:
        value = 0  
    else:
        value = 1

    url = f"http://{server_ip}/pandar.cgi?action=set&object=lidar_data&key=standbymode&value={value}"

    try:
        response = requests.get(url)
        success = 200 <= response.status_code < 300  # Successful responses are between 200 and 299
        if success:
            message = "Request sent successfully."  
        else:
            message = "Failed to send request."
        return SetBoolResponse(success, message)
    except Exception as e:
        rospy.logerr(f"Erreur : {e}")
        return SetBoolResponse(success=False)

def main():
    rospy.init_node("hesai_sleep_mode_server")
    service = rospy.Service("sensor_status", SetBool, handle_sensor_status)
    rospy.loginfo("Service SensorStatus ready.")
    rospy.spin()

if __name__ == "__main__":
    main()