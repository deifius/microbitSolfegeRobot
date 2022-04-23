from microbit import display, Image, button_a, button_b
from time import sleep

HOURS = [Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,Image.CLOCK9,Image.CLOCK10,Image.CLOCK11,Image.CLOCK12,]

def time_forward():
    for e in HOURS:
        display.show(e)
        sleep(1)
        
def time_backward():
    HOURS.reverse()
    time_forward()
    HOURS.reverse()

while True:
    display.show(Image.CLOCK12)
    if button_a.is_pressed(): time_backward()
    if button_b.is_pressed(): time_forward()