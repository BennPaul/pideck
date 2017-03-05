### select tracks via rotary encoder ###
# needs the follwoing components: 
# xdotool: sudo apt-get install xdotool
# RPi.GPIO for python: https://sourceforge.net/p/raspberry-gpio-python/wiki/install/ 
# KY040 for python: https://github.com/conradstorz/KY040 
# run it with sudo
### have fun ###

import RPi.GPIO as GPIO
from KY040 import KY040
import os, time
 
 
def rotaryTrack(direction):
    if direction == 1:
        os.system("wmctrl -a xwax")
        os.system("xdotool key \"Up\"")
    else:
        os.system("wmctrl -a xwax")
        os.system("xdotool key \"Down\"")
def buttonTrack(load):
    load = os.system("xdotool key \"F1\"")
 
 
if __name__ == "__main__":

### enter your GPIO numbers 
    CLOCKPIN = 5
    DATAPIN = 6
    SWITCHPIN = 13
   
    
    GPIO.setmode(GPIO.BCM)
    
    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryTrack, buttonTrack)
 
    ky040.start()
 
    try:
        while True:
            time.sleep(0.15)
    finally:
        ky040.stop()
        GPIO.cleanup()
 
