import pigpio
import time

class Motor():

    # max_throttle = 2000
    # min_throttle = 1000

    ### FUNCTIONS ###
    def __init__(self):
        self.pi = pigpio.pi('192.168.86.27', 8888)
        
    def configure(self, pin, placement, max_throttle, min_throttle):
        self.pi.set_servo_pulsewidth(pin, 0)
        print(placement)
        print("Disconnect battery. Enter when finished.")
        inpt = input()
        if inpt == "":
            self.pi.set_servo_pulsewidth(pin, max_throttle)
            print("Set to MAX. Listen for special tone 123 and battery beeps.")
            time.sleep(2)
            print("Once beeps twice, latched max throttle. Enter.")
            inpt = input()
            if inpt == "":
                self.pi.set_servo_pulsewidth(pin, min_throttle)
                time.sleep(1)
                print("Long Beeeep indicates latched zero position of throttle.")

    def arm(self, pin, max_throttle, min_throttle):
        self.pi.set_servo_pulsewidth(pin, max_throttle)
        time.sleep(2)
        self.pi.set_servo_pulsewidth(pin, min_throttle)
        time.sleep(1)

    def run(self, pin, throttle):
        self.pi.set_servo_pulsewidth(pin, throttle)

    def zero(self, pin):
        self.pi.set_servo_pulsewidth(pin, 0)
