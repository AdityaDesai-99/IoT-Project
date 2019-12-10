from project.Modules.gdrive_functions import Gdrive

# Making separate directory to store the videos
print("All your Sureillance feeds will be uploaded on the drive linked above!!!")
Gdrive().makeDir("SURVEILLANCE  VIDEOS")

# Adding email address of user and sharing folder with him/her
Gdrive().addEmails(input("Enter all USER email addresses : ").split())
