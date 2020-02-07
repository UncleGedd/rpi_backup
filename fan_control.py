#!/usr/bin/python3

from gpiozero import OutputDevice, CPUTemperature
from time import sleep
from datetime import datetime
from os import getpid

file = '/home/pi/fan_control.log'

with open(file, 'a+') as logfile:
	logfile.write('Running: PID ' + str(getpid())  + '\n')

pin = OutputDevice(14) # bash pinout to see pin numbers
cpu_temp = CPUTemperature().temperature # fahrenheit

while True:
    sleep(60)
    if (cpu_temp > 160):
        pin.on()
        with open(file, 'a+') as logfile:
            logfile.write('HOT! ' + str(datetime.now()) + '\n')
    else:
        pin.off()
