from picamera import PiCamera
camera = PiCamera()
import time
import os.path
from os import path
from pathlib import Path

class Aerial_Camera():

    def __init__(self):
        self.camera = camera

    def set_up(self):
        pass

    def does_file_exist(self, type_file):
        is_exist = True
        n = 0
        while is_exist == True:
            this_file = type_file + '_' + str(n)
            print(Path(this_file).is_file())
            if Path(this_file).is_file() == True:
                print('----------file exists ' + str(n) + '-----------')
                n += 1
            else:
                is_exist = False
        print('done')
        self.this_file = this_file
        return self.this_file

    def idle(self):
        self.set_up()
        self.camera.start_preview()

    def take_photo(self):
        self.set_up()
        self.does_file_exist('photo')
        self.camera.capture(self.this_file, 'jpeg', False, None, 0, True)
        time.sleep(10)
        self.camera.close()

    def record_vid(self):
        self.set_up()
        self.camera.start_recording('video_album', 'h264', None, 1)
        time.sleep(5000)
        self.camera.stop_recording()
        self.camera.close()

    def close(self):
        self.camera.close()
