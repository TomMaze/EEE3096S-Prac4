#!/usr/bin/python

#Declaration of libraries 
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

GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(freq, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(display, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
