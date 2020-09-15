# libraries
import os
import sys
import time

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems/motor.py')

# other files
from motor import Motor

class Cockpit_Motor():

    def __init__(self):
        ### PREPARE PIGPIO ###
        self.motor = Motor()
        self.motor.arm(12, 2000, 1000)
        time.sleep(2)

    def convert_percent(percent):
        self.output = 10 * int(percent) + 1000
        return self.output

    def run(self, length, speed): # seconds
        t = 0
        length = int(length)
        #speed = self.convert_percent(percent)
        while length > t:
            self.motor.run(12, speed)
            t += 1
            time.sleep(1)
            #self.motor.zero()

    def stop(self):
        self.motor.zero()
