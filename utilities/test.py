#!/bin/python
import time
import RPi.GPIO as GPIO

#set up GPIO
GPIO.setmode(GPIO.BCM)

Motor1A = 23
Motor1B = 24
Motor1E = 25

GPIO.setwarnings(False)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

print "Closing"


GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

time.sleep(2)



print "Opening"


GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

time.sleep(2)

print "Stop"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.cleanup()
