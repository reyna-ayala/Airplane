# libraries
import os
import sys

# Linux path
sys.path.append('./subsystems')

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems')

# subsystems
from motor import Motor

class Configure():
    
    def __init__(self):
        ### INSTANTIATE ###
        self.cockpit = Motor()

        ### CALIBRATE ###
        self.cockpit.configure(12, "COCKPIT", 2000, 1000)

config = Configure()
