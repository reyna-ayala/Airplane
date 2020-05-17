import RPi.GPIO as GPIO
import time

class Servo():
    ### VARS TO SET ###
    # self.pin_num
    # angle
    # rest

    def set_up(self, pin_num):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_num, GPIO.OUT)
        self.servo = GPIO.PWM(pin_num, 50) # arbitrary Hz

    def initialize(self, pin_num):
        self.set_up(pin_num)
        self.servo.start(60)
        time.sleep(2)

    def set_angle(self, pin_num, angle, rest):
        #self.set_up(pin_num)
        self.servo.ChangeDutyCycle(2 + (angle / 18))
        time.sleep(rest)
        self.servo.ChangeDutyCycle(0)
        self.servo.stop()

