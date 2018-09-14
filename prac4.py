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
