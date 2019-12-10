from datetime import datetime
import os
import time

from picamera import PiCamera

from project.Modules.GPIOfunctions import pirInput

videoPath = ''
imageDate = ''

class Camera:
    camera = None

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)
        time.sleep(2)

    def captureImages(self):
        os.mkdir("Images")
        global imageDate
        imageDate = "{}".format(datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        for i in range(10):
            self.camera.capture("Images//image{:>2d}.png".format(i), format='PNG')
            if not pirInput():
                break
            time.sleep(1)


    def captureStream(self):

        os.mkdir("Video")
        global videoPath
        videoPath = '../Video/' + datetime.now().strftime("%H:%M:%S  %d-%m-%Y")
        self.camera.start_recording(videoPath + '.h264')

        while pirInput():
            self.camera.wait_recording(1)
            time.sleep(1)

        self.camera.wait_recording(5)
        self.camera.stop_recording()

        os.popen("MP4Box -add {0}.h264 {0}.mp4".format(videoPath))
        #os.remove(videoPath + '.h264')
