# outline
    # initiliaze subsystems
    # instantiate subsystems
    # execute (scheduler?)

# libraries
import os
import sys
import RPi.GPIO as GPIO
import time

# Linux path
sys.path.append('./subsystems')

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems')

# subsystems
from left_control_pitch import Left_Control_Pitch
from right_control_pitch import Right_Control_Pitch
from left_wing_flap import Left_Wing_Flap
from right_wing_flap import Right_Wing_Flap
#from aerial_camera import Aerial_Camera
from cockpit_motor import Cockpit_Motor

class Airplane():

    def __init__(self):
        ### VARS ###
        
        ### INSTANTIATE SUBSYSTEMS ###
#        self.aerial_camera = Aerial_Camera()
        self.cockpit_motor = Cockpit_Motor()

        ### INITIALIZE SUBSYSTEMS ###

    def periodic(self):
        ### RUN EXECUTE METHODS ###
        self.cockpit_motor.run(1, 1200)

#        try:
#            self.aerial_camera.record_vid(2)
#        finally:
#            self.aerial_camera.close()

plane = Airplane()
plane.periodic()
GPIO.cleanup()
#plane.cockpit_motor.stop()
