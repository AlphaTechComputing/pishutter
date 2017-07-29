#!/bin/python
import datetime
import time
import pytz
import dateutil.parser
from astral import Astral

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


#print "Sunrise: " + str(sunrise_parsed)
#print "Sunset: " + str(sunset_parsed)
#print "Current: " + str(current_parsed)

def main():
    while True:
	#before sunrise
	if sunrise_parsed <= current_parsed >= sunset_parsed:
		print "after sunrise and before sunset; closing filter"
		time.sleep(30)

	if sunset_parsed >= current_parsed <= sunrise_parsed:
                print "after sunset and before sunrise opening filter"
		time.sleep(30)

	else:
		print "you screwed it up!"
		time.sleep(30)



if __name__ == '__main__':
    main()
    time.sleep(1)
    exit(0)
