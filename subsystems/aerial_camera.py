from picamera import PiCamera

class Aerial_Camera():

    def __init__(self):
        self.camera = PiCamera()

    def set_up(self):
        pass

    def idle(self):
        try:
            self.set_up()
            self.camera.start_preview()
        finally:
            self.camera.stop_preview()
            self.camera.closer()

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
