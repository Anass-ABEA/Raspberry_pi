# imports
from gpiozero import LED
import time


# LEDs Setup
red_led = LED(23)
gre_led = LED(24)
ora_led = LED(25)

# set up Mode
def on_off(led,v):
    # on GPIO.output(led_pin,GPIO.HIGH) & wait
    led.on()
    time.sleep(v)
    # off GPIO.output(led_pin,GPIO.LOW) & wait
    led.off()
    time.sleep(v)

def blink_led(led):
    # allumer pour 2 seconde et clignoter pour 1 seconde

    # on : GPIO.output(led_pin,GPIO.HIGH)
    led.on()
    time.sleep(2)
    # off : GPIO.output(led_pin,GPIO.LOW)
    led.off()
    for i in range (4):
        on_off(led,0.125)

i=0
while True:
    on_off(red_led,1)
    blink_led(gre_led)
    on_off(ora_led,1)
    print("loop ",i)
    i+=1