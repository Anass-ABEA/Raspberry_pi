# imports
from gpiozero import LED,Button
import time

#LED
led = LED(14)
button = Button(21)


# la led s'allume et s'éteint rappidement donc on ne constate pas (à l'oeil nu) que la LED s'éteint
while(True):
    led.off()
    if button.is_pressed:
        led.on()