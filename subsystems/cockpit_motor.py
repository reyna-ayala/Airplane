# libraries
import os
import sys
import time
#from gpiozero import PWMOutputDevice

# RPi path
#sys.path.insert(0, '/home/reyna/Airplane/subsystems/motor.py')
sys.path.insert(0, '/home/reyna/Airplane/subsystems/motor_pigpio.py')

# other files
#from motor import Motor
from motor_pigpio import Motor_Pigpio

class Cockpit_Motor():

    def __init__(self):
        ### PREPARE PIGPIO ###
        self.motor = Motor_Pigpio()
        self.motor.arm(18)
        time.sleep(2)

    def run_half_speed(self, rest):
        self.motor.run(18, 50, 1500)
        time.sleep(rest)
