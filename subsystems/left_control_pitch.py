# libraries
import RPi.GPIO as GPIO
import time

class Left_Control_Pitch():

    def __init__(self):
        ### IS INIT? ###
        f = open("log_file.txt", "w")
        f.write("left_control_pitch init !!")
        f.close()

        ### VARIABLES ###
        p = None
        self.is_ready = False
        self.old_time = time.time()

        ### PREPARE PWM ###
        servo_pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.p = p
        self.p = GPIO.PWM(servo_pin, 100) #arbitrary Hz

        self.p.start(0.3)
        time.sleep(0.15)
        self.p.ChangeDutyCycle(0)
        time.sleep(1)

    def level(self):
        self.p.ChangeDutyCycle(1)
        time.sleep(0.15)

    def up():
        pass

    def down():
        pass
