import shutil, os
import base64

from sendgrid import SendGridAPIClient, Attachment
from sendgrid.helpers.mail import Mail
from project.Modules.Camera import imageDate
from project import getData


class Mailing:
    sendgrid_client = SendGridAPIClient(getData('SENDGRID_API_KEY'))
    message = None

    def __init__(self):
        self.message = Mail(
            from_email=('nike990701@gmail.com', 'Raspberry Pi'),
            to_emails=getData('emails'),
            subject='Someone\'s at your door!!',
            html_content=f"<strong>This person was at your door at {imageDate} </strong>"
        )

    def sendEmail(self):
        for r, d, f in os.walk('Images'):
            for file in f:
                img_data = open(file, "rb").read()
                encoded = base64.b64encode(img_data).decode()
                self.message.add_attachment(Attachment(encoded, os.path.basename(file.name), "image/png"))
                img_data.close()

        self.sendgrid_client.send(self.message)
        # shutil.rmtree('Images')