# libraries
import os
import sys

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems/')

# other files
from servo import Servo

class Right_Control_Pitch():

    def __init__(self):
        ### PREPARE PWM ###
        self.servo = Servo()
        self.servo.initialize(17)

    def level(self):
        self.servo.run(9.7, 1) # turn towards 90, 1 is rest

    def up(self):
        self.servo.run(12.5, 1) # turn towards 0

    def down(self):
        self.servo.run(6, 1) # turn towards down
