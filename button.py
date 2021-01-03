# imports
from gpiozero import LED,Button
import time

#LED
button = Button(21)


# la led s'allume et s'éteint rappidement donc on ne constate pas (à l'oeil nu) que la LED s'éteint
while(True):
    button.wait_for_press()
    print("boutton cliqué !!")
    time.sleep(0.5)
    