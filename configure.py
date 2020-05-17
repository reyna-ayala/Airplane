# libraries
import os
import sys

# Linux path
sys.path.append('./subsystems')

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems')

# subsystems
from motor_pigpio import Motor_Pigpio

class Configure():
    
    def __init__(self):
        ### INSTANTIATE ###
        self.cockpit = Motor_Pigpio()

        ### CALIBRATE ###
        self.cockpit.calibrate(18)

config = Configure()
