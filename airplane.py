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

class Airplane():

    def __init__(self):
        ### IS INIT? ###
        f = open("log_file.txt", "w")
        f.write("test init")
        f.close()
        
        ### INSTANTIATE SUBSYSTEMS ###
        left_control_pitch = Left_Control_Pitch()
        self.left_control_pitch = left_control_pitch

        ### INITIALIZE SUBSYSTEMS ###
        self.left_control_pitch.__init__()

    def periodic(self):
        ### RUN EXECUTE METHODS ###
        self.left_control_pitch.level()

Airplane.__init__(self)
Airplane.periodic()