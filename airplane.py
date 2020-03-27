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
sys.path.insert(0, '/home/ubuntu/airplane/subsystems')

# subsystems
from left_control_pitch import Left_Control_Pitch
from aerial_camera import Aerial_Camera

class Airplane():

    def __init__(self):
        ### IS INIT? ###
        f = open("log_file.txt", "w")
        f.write("test init")
        f.close()
        
        ### INSTANTIATE SUBSYSTEMS ###
        self.left_control_pitch = Left_Control_Pitch()
        self.aerial_camera = Aerial_Camera()

        ### INITIALIZE SUBSYSTEMS ###
        self.left_control_pitch.__init__()
        self.aerial_camera.__init__()

    def periodic(self):
        ### RUN EXECUTE METHODS ###
        #self.left_control_pitch.level()
        #self.left_control_pitch.up()
        self.aerial_camera.idle()

plane = Airplane()
plane.__init__()
plane.periodic()
