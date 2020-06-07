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

    def run_half_speed(self, length): # seconds
        t = 0
        length = int(length)
        while length > t:
            self.motor.run(12, 1500)
            t += 1
            time.sleep(1)

    def stop(self):
        self.motor.zero()
