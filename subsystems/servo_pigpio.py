import pigpio
import time

class Servo_Pigpio():

    def __init__(self):
        self.pig = pigpio
        self.servo = pigpio.pi

    def initialize(self, pin_num, freq):
        self.servo.set_mode(pin_num, self.pig.OUTPUT)
        self.servo.set_PWM_frequency(pin_num, freq)
        time.sleep(1)

    def run(self, pin_num, new_freq):
        self.servo.set_PWM_frequency(pin_num, new_freq)
