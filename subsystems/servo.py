import RPi.GPIO as GPIO
import time

class Servo():
    ### VARS TO SET ###

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def initialize(self, pin_num, init_pos):
        GPIO.setup(pin_num, GPIO.OUT)
        self.pwm = GPIO.PWM(pin_num, 50)
        self.pwm.start(init_pos)
        time.sleep(0.5)

    def run(self, duty, rest):
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(rest)
