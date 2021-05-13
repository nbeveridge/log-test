import time

import RPi.GPIO as GPIO
from hx711 import HX711


class sensor:
        def __init__(self,SensorPins):
            self.SensorPins = SensorPins                

            # pub = rospy.Publisher(balloon_type+'_balloon_sensor_node_pub', Int64, queue_size=1)
            # rospy.init_node(balloon_type+'_balloon_sensor_node_pub', anonymous=True)
            # rate = rospy.Rate(250) # 10hz
            # HOW TO CALCULATE THE REFFERENCE UNIT
            # To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
            # In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
            # and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
            # If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
            #hx.set_reference_unit(113)
            referenceUnit = 100
            offset =  0
            out = SensorPins[0]
            sck = SensorPins[1]
            self.hx = HX711(out, sck)
            self.hx.set_reading_format("MSB", "MSB")
            self.hx.set_reference_unit(referenceUnit)
            self.hx.reset()
            self.hx.tare()
            # after tareing to set the pressure to zero the desired offset is added to the tare offset
            tare_off = self.hx.get_offset()
            self.hx.set_offset(tare_off+offset*referenceUnit)

            # while not rospy.is_shutdown():
            #     pub_state = self.read_sensor_test()
            #     pub.publish(pub_state)
            #     rate.sleep()

        def read_sensor_test(self):
            val = self.hx.get_weight(5)  #  get_weight(5) averages the weight from 5 samples
#             self.hx.power_down()
#             self.hx.power_up()
            return int(val)

def test():
    sen = sensor([5,6])
    while(True):
        start = time.time()

        sen.read_sensor_test()

        end = time.time()

        print(f"Runtime of the program is {(end - start)/5}")
