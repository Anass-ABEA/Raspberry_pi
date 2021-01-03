from gpiozero import LED
import time

#LED
led = LED(25)


while True:
    # on : GPIO.output(led_pin,GPIO.HIGH)
    led.on()
    time.sleep(0.5)
    # off : GPIO.output(led_pin,GPIO.LOW)
    led.off()
    time.sleep(0.5)
