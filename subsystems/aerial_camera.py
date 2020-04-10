from picamera import PiCamera
camera = PiCamera()
import time

class Aerial_Camera():

    def __init__(self):
        self.camera = camera

    def set_up(self):
        pass

    def idle(self):
        self.set_up()
        self.camera.start_preview()

    def take_photo(self):
        self.set_up()
        self.camera.capture('photo_album', 'jpeg', False, None, 0, True)
        time.sleep(10)
        self.camera.close()

    def record_vid(self):
        self.set_up()
        self.camera.start_recording('video_album', 'h264', None, 1)
        time.sleep(5000)
        self.camera.stop_recording()
        self.camera.close()
