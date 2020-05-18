import RPi.GPIO as GPIO
import time
from gpiozero import PWMLED


led = PWMLED(21)

def loop():
    
    GPIO.setmode(GPIO.BCM)

    ##assigning pins to trigger and echo
    TRIG = 4
    ECHO = 18

    GPIO.setup(TRIG, GPIO.OUT)##trigger pin the output pin
    GPIO.output(TRIG, 0)##trigger pin set low

    GPIO.setup(ECHO, GPIO.IN)##echo pin the input pin

    time.sleep(0.1)##short delay for sensor to settle down

    print ("starting measurement")
    
    ##sensor fires the signal in this upcoming step
    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
            pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
            pass
    stop = time.time()

    distance = (stop - start) * 170
    print(distance)

    led.pulse()
    led.value = (1 - distance) ##distance more brightness less
    time.sleep(1)

try:    
    while True:
        loop()
except KeyboardInterrupt:
    GPIO.cleanup()
