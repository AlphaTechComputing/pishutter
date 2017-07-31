#!/bin/python
import RPi.GPIO as GPIO

#set up GPIO
Motor1A = 23
Motor1B = 24
Motor1E = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

def open_filter():

        if return_filter_state() == opened:
                print "Filter is already open."

        else:
                GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor1B,GPIO.HIGH)
                GPIO.output(Motor1E,GPIO.HIGH)

def close_filter():

        if return_filter_state() == closed:
                print "Filter is already open."

        else:
                GPIO.output(Motor1A,GPIO.HIGH)
                GPIO.output(Motor1B,GPIO.LOW)
                GPIO.output(Motor1E,GPIO.HIGH)



def main():

	response = raw_input("Would you like to open or close the filter? O/C")

        try:

            if response == "O":
                open_filter()

            if response == "C":
                close_filter()

        finally:
                GPIO.cleanup()


if __name__ == '__main__':
    main()
    exit(0)

