# outline
    # initiliaze subsystems
    # instantiate subsystems
    # execute (scheduler?)

# libraries
import os
import sys

# Linux path
sys.path.append('./subsystems')

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems')

# subsystems
#from left_control_pitch import Left_Control_Pitch
#from aerial_camera import Aerial_Camera
from cockpit_motor import Cockpit_Motor

class Airplane():

    def __init__(self):
        ### VARS ###
        
        ### INSTANTIATE SUBSYSTEMS ###
#        self.left_control_pitch = Left_Control_Pitch()
#        self.aerial_camera = Aerial_Camera()
        self.cockpit_motor = Cockpit_Motor()

        ### INITIALIZE SUBSYSTEMS ###

    def periodic(self):
        ### RUN EXECUTE METHODS ###
        #self.left_control_pitch.level()
        #self.left_control_pitch.up()
        #self.aerial_camera.idle()
        #self.aerial_camera.take_photo()
        #self.aerial_camera.record_vid()
        self.cockpit_motor.run_half_speed(5)

plane = Airplane()
plane.periodic()
