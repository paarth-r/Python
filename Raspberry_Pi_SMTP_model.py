import RPi.GPIO as GPIO
import smtplib

#initialize smtp session
s = smtplib.SMTP(host='smtp-mail.outlook.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(" new outlook account address", "pasword for new outlook account")


#specify pin number(must be GPIO)
BEAM_PIN = 17
alrbroken = False
def break_beam_callback(channel):
#checking for input
    if GPIO.input(BEAM_PIN):
#set that the beam has not already been broken
#check if beam has already been broken to prevent spam
        if not alrbroken:
          s.sendmail("your outlook email address", "your home email address")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)
Message = input("DO NOT PRESS ANYTHING, ESPECIALLY NOT ENTER. I SWEAR TO GOD\n")
GPIO.cleanup()
