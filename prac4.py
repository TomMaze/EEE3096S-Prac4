#!/usr/bin/python

#Declaration of libraries 
import spidev
import time
import datetime
import os
import RPi.GPIO as GPIO

#GPIO pins setup
GPIO.setmode(GPIO.BCM)
reset =17
freq =27
stop =22
display=23

#setup for interrupt switches
GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(freq, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(display, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

# Define sensor channels
light_channel = 0
temp_channel  = 1
pot_channel= 2
<<<<<<< HEAD
=======

	
# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
# Function to calculate temperature from
# MCP9700A data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
  temp = (((data * 3.30)/float(1023))-0.50)/0.01
  temp = round(temp,places)
  return temp

#function generating a string to display time and timer in the correct format
def TimeFormat(t):
	timeinstance=time.localtime(t)
	return(str(timeinstance.tm_min).zfill(2)+":"+str(timeinstance.tm_sec).zfill(2)+":"+str(t-int(t))[2:4]) 

#function to convert light incident to LDR to a percent
def ConvertLight(data, places):
	vOut=(data*3.3)/float(1023)
	light=vOut/3.3*100
	light=round(light,places)
	return light

<<<<<<< HEAD
>>>>>>> Tom
=======

#reset callback function definition
def resetcallback(channel):
	global starttime
	global log5
	global logcount
	starttime=time.time()
	log5=""
	logcount=0

#frequency callback function definition
def freqcallback(channel):
	global delay
	if (delay==0.5):
		delay=1
	elif (delay==1):
		delay=2
	elif (delay==2):
		delay=0.5

#stop callbaack function def
def stopcallback(channel): 
	global monitor
	global logcount
	if (monitor==1):
		monitor=0
	elif (monitor==0):
		monitor=1
		logcount=0

#display callback function def
def displaycallback(channel):
	global monitor
	global log5
	if (monitor==0):
		print("Time     Timer    Pot  Temp   Light")
		print(log5)
    
#Under a rising edge, the callback function is called 
GPIO.add_event_detect(reset,	GPIO.RISING,	callback=resetcallback,	bouncetime=200)
GPIO.add_event_detect(freq,	GPIO.RISING,	callback=freqcallback, bouncetime=200)
GPIO.add_event_detect(stop,	GPIO.RISING,	callback=stopcallback, bouncetime=200)
GPIO.add_event_detect(display,	GPIO.RISING,	callback=displaycallback, bouncetime=200)

#Display on/off variable
monitor=1

#Default display frequency
delay=0.5

#variable of initial start time, used for timer
starttime=time.time()

#variable to limit readings shown in display function
logcount=0

#define log and log 5(for display) as a global string
log=""
log5=""
>>>>>>> Tom
