#!/usr/bin/env python

from microbit import *
from time import sleep
import random

oldbright = 0

def displBright(brightness, oldbright):
    if brightness > oldbright:
    	for e in range(oldbright, brightness):
    	    image = Image(5,5, bytearray([int(e/11),int(e/10),int(e/9.5),int(e/10),int(e/11),int(e/9),int(e/8),int(e/7.5),int(e/8),int(e/9),int(e/7),int(e/6),int(e/5.5),int(e/6),int(e/7),int(e/5),int(e/4),int(e/3.5),int(e/4),int(e/5),int(e/3),int(e/2),int(e),int(e/2),int(e/3),]))
    	    display.show(image)
    	    sleep(.1)
    	return brightness
    else:
    	for e in range(oldbright*-1, brightness*-1):
    	    e = e * -1
    	    image = Image(5,5, bytearray([int(e/11),int(e/10),int(e/9.5),int(e/10),int(e/11),int(e/9),int(e/8),int(e/7.5),int(e/8),int(e/9),int(e/7),int(e/6),int(e/5.5),int(e/6),int(e/7),int(e/5),int(e/4),int(e/3.5),int(e/4),int(e/5),int(e/3),int(e/2),int(e),int(e/2),int(e/3),]))
    	    display.show(image)
    	    sleep(.1)
    	return brightness

while True: 
    oldbright = displBright(random.randint(0,100), oldbright)


