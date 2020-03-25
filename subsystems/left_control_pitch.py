# libraries
import RPi.GPIO as GPIO

class Left_Control_Pitch():

    def __init__(self):
        ### IS INIT? ###
        f = open("log_file.txt", "w")
        f.write("left_control_pitch init !!")
        f.close()

        ### VARIABLES ###
        p = None

        ### PREPARE PWM ###
        servo_pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.p = p
        self.p = GPIO.PWM(servo_pin, 50) #arbitrary Hz
        self.p.start(2.5)

    def level(self):
        self.p.ChangeDutyCycle(5)

    def up():
        pass

    def down():
        pass
