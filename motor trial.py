import RPi.GPIO as GPIO
import time


servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(0.1)
try:
    while True:
        p.ChangeDutyCycle(0.2)
        time.sleep(0.5)
        p.ChangeDutyCycle(0.3)
        time.sleep(0.5)
        p.ChangeDutyCycle(0.4)
        time.sleep(0.5)
       # p.ChangeDutyCycle(25) #
        #time.sleep(0.5) #
        #p.ChangeDutyCycle(20) #
        # time.sleep(0.5) 
        p.ChangeDutyCycle(0.3)
        time.sleep(0.5)
        p.ChangeDutyCycle(0.2)
        time.sleep(0.5)
        p.ChangeDutyCycle(0.1)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
