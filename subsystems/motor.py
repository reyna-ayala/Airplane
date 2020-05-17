# libraries
from gpiozero import PWMOutputDevice
import time

class Motor():
    
    def __init__(self):
        pass

    def set_up(self, ojb, pin_num):
#        self.close = PWMOutputDevice.close(self)
        self.motor = ojb(pin_num, True, 0.5, 100, None)

    def run(self, rest):
        self.motor.on()
        time.sleep(rest)
        self.motor.close()
