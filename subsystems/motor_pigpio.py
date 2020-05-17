# libraries
import pigpio
import time

class Motor_Pigpio():

    ### define ###
    
    # duty cycle
    # frequency

    def __init__(self):
        self.pi = pigpio.pi()
        print(self.pi.connected)
        # successfully prints 'True'

    def max_val(self, pin_num):
        self.pi.set_servo_pulsewidth(pin_num, 2000)

    def min_val(self, pin_num):
        self.pi.set_servo_pulsewidth(pin_num, 700)

    def calibrate(self, pin_num):
        self.pi.set_mode(pin_num, 1)
        self.pi.set_servo_pulsewidth(pin_num, 0)
        time.sleep(1)
        inpt = input()
        if inpt == '':
            self.max_val(pin_num)
            print("Connect BATTERY now. Wait for 2 beeps. Enter.")
            inpt = input()
            time.sleep(1)
            if inpt == '':
                self.min_val(pin_num)
                print("Special tone")
                time.sleep(7)
                print("Just wait...")
                time. sleep(5)
                self.pi.set_servo_pulsewidth(pin_num, 0)
                time.sleep(2)
                print("ARMING")
                time.sleep(1)

    def arm(self, pin_num):
        # minimum throttle
        self.min_val(pin_num)
        time.sleep(1)
        self.max_val(pin_num)
        time.sleep(1)

    def run(self, pin_num, freq, throttle):
#        self.pi.set_PWM_range(pin_num, 255)
        self.pi.set_PWM_frequency(pin_num, freq)
#        self.pi.set_PWM_dutycycle(pin_num, dc)
        self.pi.set_servo_pulsewidth(pin_num, throttle)

    def end_run(self):
        #self.pi.stop()
        pass
