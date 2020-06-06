# libraries
import os
import sys

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems/')

# other files
from servo import Servo

class Left_Wing_Flap():

    def __init__(self):
        ### PREPARE PWM ###
        self.servo = Servo()
        self.servo.initialize(18)

    def level(self):
        self.servo.run(1.4, 1) # turn towards 90, 1 is rest

    def down(self):
        self.servo.run(6, 1) # turn towards down
