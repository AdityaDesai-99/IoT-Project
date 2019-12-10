import os

from project import getData, updateData

rqrdfiles = os.getcwd() + '//required_files//'
gdrive = "gdrive"

class Gdrive:
    # Makes a directory in Google Drive and returns its ID
    def makeDir(folder):
        data = {}
        cmd = '{} mkdir "{}"'.format(gdrive, folder)
        res = os.popen(cmd).read().split()[1]

        updateData('parent', res)

        return getData('parent')

    # Add the USER email for sharing the drive
    def addEmails(emails):
        updateData('emails', emails)

        # Sharing the Drive folder with USER
        for email in getData('emails'):
            cmd = f"{gdrive} share {getData('parent')} --type user --email {email}"
            os.popen(cmd)


    def upload(filePath):
        parent = getData('parent')
        os.popen('{} upload --parent {} "{}"'.format(gdrive, parent, filePath))


