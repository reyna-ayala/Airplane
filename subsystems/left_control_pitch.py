# libraries
import os
import sys

# RPi path
sys.path.insert(0, '/home/ubuntu/airplane/subsystems/servo.py')

# other files
from servo import Servo

class Left_Control_Pitch():
    
    def __init__(self):
        ### IS INIT? ###
        f = open("log_file.txt", "w")
        f.write("left_control_pitch init !!")
        f.close()

        ### PREPARE PWM ###
        self.servo = Servo()
        self.servo.initialize(17)
        #self.servo.set_angle(60, 5)

    def level(self):
        self.servo.set_up(17)
        self.servo.set_angle(60, 0.5)

    def up(self):
        self.servo.set_up(17)
        self.servo.set_angle(30, 0.5)

    def down(self):
        pass
