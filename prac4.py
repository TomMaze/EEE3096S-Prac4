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

>>>>>>> Tom
