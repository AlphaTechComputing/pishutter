#!/bin/python
import datetime
import time
import pytz
import dateutil.parser
from astral import Astral
import RPi.GPIO as GPIO

#set up GPIO
Motor1A = 23
Motor1B = 24
Motor1E = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

# Location variables
city_name = 'Columbus'
timezone = 'US/Eastern'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]

#Time variables
today =  datetime.datetime.now()
current_time = datetime.datetime.now(pytz.timezone(timezone))
year =  int(today.year)
month = int(today.strftime("%m"))
day = int(today.strftime("%d"))
second = int(today.strftime("%M"))
sun = city.sun(date=datetime.date(year, month, day), local=True)
sunrise_datetime = str(sun['sunrise'])
sunset_datetime = str(sun['sunset'])
sunrise_parsed = dateutil.parser.parse(str(sunrise_datetime))
sunset_parsed = dateutil.parser.parse(str(sunset_datetime))
current_parsed = dateutil.parser.parse(str(current_time))


#Check what filter status needs to be based on current time, sunrise, and sunset
def return_filter_time():

	print "Sunrise: " + str(sunrise_parsed)
	print "Sunset: " + str(sunset_parsed)
	print "Current: " + str(current_parsed)

	if sunrise_parsed <= current_parsed <= sunset_parsed:
		print "after sunrise this morning and before sunset today; filter should be closed"
		return "close"

	if sunset_parsed <= current_parsed <= sunrise_parsed:
                print "after sunset and before sunrise this morning. filter should be opened"
		return "open"

	if sunset_parsed <= current_parsed and sunrise_parsed <= current_parsed:
                print "after sunset today and before sunrise next morning. filter should be opened"
                return "open"

	if sunrise_parsed >= current_parsed and sunset_parsed >= current_parsed:
		print "before sunrise and sunset today. filter should be opened"
		return "open"

	else:
		raise Exception('Logical error with return_filter_time function')



def open_filter():

		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.HIGH)
		time.sleep(5)
		print "Filter opened"

def close_filter():


		GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor1B,GPIO.HIGH)
                GPIO.output(Motor1E,GPIO.HIGH)
		time.sleep(5)
		print "Filter closed"


def main():

	try:
	  while True:
	    if return_filter_time() == "open":
		open_filter()
		time.sleep(300)

	    if return_filter_time() == "close":
		close_filter()
		time.sleep(300)

	finally:
		GPIO.cleanup()


if __name__ == '__main__':
    main()
    exit(0)
