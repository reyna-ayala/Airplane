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
from aerial_camera import Aerial_Camera
from cockpit_motor import Cockpit_Motor

class Airplane():

    def __init__(self):
        ### VARS ###
        
        ### INSTANTIATE SUBSYSTEMS ###
        self.left_control_pitch = Left_Control_Pitch()
#        self.aerial_camera = Aerial_Camera()
        self.cockpit_motor = Cockpit_Motor()

        ### INITIALIZE SUBSYSTEMS ###

    def periodic(self):
        ### RUN EXECUTE METHODS ###
        self.left_control_pitch.level()
        self.cockpit_motor.run_half_speed(1)

#        try:
#            self.aerial_camera.record_vid(2)
#        finally:
#            self.aerial_camera.close()

plane = Airplane()
plane.periodic()
GPIO.cleanup()
Airplane.self.cockpit_motor.stop()
