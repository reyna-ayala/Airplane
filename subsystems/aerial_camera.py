from picamera import PiCamera
camera = PiCamera()
import time
import sys, termios, tty, os

class Aerial_Camera():

    def __init__(self):
        self.camera = camera

    def set_up(self):
        pass

    def idle(self):
        self.set_up()
        self.camera.start_preview()

        while True:
            time.sleep(1000)
            char = getch()
            if (char == 'e'):
                self.camera.stop_preview()
                self.camera.close()

    def take_photo(self):
        try:
            self.set_up()
            self.camera.capture('photo_album', 'jpeg', False, None, 0, True)
        finally:
            self.camera.close()

    def record_vid(self):
        try:
            self.set_up()
            self.camera.start_recording('video_album', 'h264', None, 1)
        finally:
            self.camera.stop_recording()
            self.camera.close()

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattre(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
