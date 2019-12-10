import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)


# Setting up the PIR sensor
pirPIN = 15
gpio.setup(pirPIN, gpio.IN)

def pirInput():
    return gpio.input(pirPIN)
