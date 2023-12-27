import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

in1 = 23
in2 = 24

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

while True:
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    time.sleep(2)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    time.sleep(2)
    

    