# imports
from gpiozero import LED,Button
import time
import random

#LED
led = LED(21)
button_1 = Button(14)
button_2 = Button(15)

# ressayer encore
def reset():
    led.off()
    print(score)
    while (not button_1.is_pressed and (not button_2.is_pressed)):
        print("Press any Button to restart")




led.off()
led_off = True
score = [0,0]
while(True):
    if(led_off):
        time.sleep(random.uniform(0.3,3))
        led_off= False
    led.on()
    if(button_1.is_pressed and button_2.is_pressed):
        print("DRAW!")
        reset()
        led_off = True
    elif (button_1.is_pressed) : # dans ce cas il est évident que boutton_2 est OFF car sinon on est dans le cas précédent.
        print("Player 1 Won!")
        score[0]+=1
        reset()
        led_off = True
    elif (button_2.is_pressed):
        print("Player 2 Won!")
        score[1]+=1
        reset()
        led_off = True
