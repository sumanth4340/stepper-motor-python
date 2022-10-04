import Adafruit_BBIO.GPIO as GPIO
import time
from time import sleep
dir="P9_15"
step="P9_12"
GPIO.setup(step,GPIO.OUT)
GPIO.setup(dir,GPIO.OUT)
while(1):
        right=0
        left=1
        exit=2
        direction=input("enter the direction\n left/right =  ")
        steps=input("enter steps =  ")
        speed=input("enter speed --\n>> if speed = 0.0005 = highspeed \n>>if speed = 0.001 = slow\n now enter>>=")
        if speed<=0.0004:
                speed=0.0005
        if speed>=0.001:
                speed=0.001
        if speed<=0.001:
                speed=0.001
        if direction == 0:
                GPIO.output(dir,GPIO.HIGH)
        if direction == 1:
                GPIO.output(dir,GPIO.LOW)
        for i in range(0,steps):
                GPIO.output(step,GPIO.HIGH)
                sleep(speed)
                GPIO.output(step,GPIO.LOW)
                sleep(speed)
        if direction == exit:
                break
print "THANKS FOR USING"
GPIO.cleanup()





