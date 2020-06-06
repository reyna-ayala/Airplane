import pigpio
import time

pin_num = 12
max_throttle = 2000
min_throttle = 1000

pi = pigpio.pi('192.168.86.27', 8888)
pi.set_servo_pulsewidth(pin_num, 0)

# CONFIGURE
print("Disconnect battery. Enter when finished.")
inpt = input()
if inpt == "":
    pi.set_servo_pulsewidth(pin_num, max_throttle)
    print("Set to MAX. Listen for special tone 123 and battery beeps.")
    time.sleep(2)
    print("Once beeps twice, latched max throttle. Enter.")
    inpt = input()
    if inpt == "":
        pi.set_servo_pulsewidth(pin_num, min_throttle)
        time.sleep(1)
        print("Long Beeeep indicates latched zero position of throttle.")

# RUN SOMETHIN
while 1:
    pi.set_servo_pulsewidth(pin_num, 1200)
