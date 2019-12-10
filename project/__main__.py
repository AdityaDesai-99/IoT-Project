import time, os, shutil
from threading import Thread
from multiprocessing import Process
from project.Modules.Camera import Camera
from project.Modules.Mailing import Mailing
from project.Modules.GPIOfunctions import pirInput
from project.Modules.gdrive_functions import Gdrive, rqrdfiles, gdrive
from project.Modules import RFID


os.popen("chmod +x {}".format(rqrdfiles + gdrive))

def rfidChecker():
    while True:
        if RFID.rfidStatus is True:
            if mail_thread.is_alive():
                mail_thread.terminate()
            if gdrive_thread.is_alive():
                gdrive_thread.terminate()
            RFID.clearFlag()
            global  rfidStatus
            rfidStatus = True
            time.sleep(10)
            break

camera = Camera.Camera()
mail = Mailing()
drive = Gdrive()

rfidStatus = False
    
while True:
    try:
        if pirInput():
            rfid_thread = Process(target=rfidChecker())
            rfid_thread.start()
            time.sleep(5)
            camera.captureImages()

            if rfidStatus is True:
                rfid_thread.terminate()
                global rfidStatus
                rfidStatus = False
                shutil.rmtree("Images")
                continue

            mail_thread = Process(target=mail.sendEmail())
            mail_thread.start()

            camera.captureStream()

            if rfidStatus is True:
                rfid_thread.terminate()
                global rfidStatus
                rfidStatus = False
                shutil.rmtree("Video")
                continue

            gdrive_thread = Process(target=drive.upload(), args=(camera.videoPath + '.mp4'))
            gdrive_thread.start()

            rfid_thread.terminate()

    except Exception as e:
        print(str(e))