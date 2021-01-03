# imports
from gpiozero import LED,Button
import time

#LED
led = LED(25)
button = Button(23)

led.off()

while(True):
    if button.is_pressed :
        print("boutton cliqué !!")
    