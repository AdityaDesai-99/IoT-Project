from mfrc522 import SimpleMFRC522

rfidStatus = False


class RFID:
    reader = None

    def __init__(self):
        self.reader = SimpleMFRC522()

    def checkRFID(self):
        while True:
            status, TagType = self.reader.read_no_block()
            if status != 'None':
                global rfidStatus
                rfidStatus = True
                break


def clearFlag():
    global rfidStatus
    rfidStatus = False
