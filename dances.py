from solfege import solfa
from speech import sing
from microbit import display, Image

"""
I am a set of relations of dance positions
to sing actions
"""

class dances:
    def up():
        display.show(Image.ARROW_N)
        sing(solfa[0], speed=100)
        #sleep(1000)
    def down():
        display.show(Image.ARROW_S)
        sing(solfa[1], speed=100)
        #sleep(1000)
    def right():
        display.show(Image.ARROW_E)
        sing(solfa[2], speed=100)
        #sleep(1000)
    def left():
        display.show(Image.ARROW_W)
        sing(solfa[3], speed=100)
        #sleep(1000)
    def face_up():
        display.show(Image.CLOCK12)
        sing(solfa[4], speed=100)
        #sleep(1000)
    def face_down():
        display.show(Image.CLOCK6)
        sing(solfa[5], speed=100)
        #sleep(1000)
    def freefall():
        display.show(Image.SURPRISE)
        sing(solfa[6], speed=400)
    def GGG():
        display.show(Image.SURPRISE)
        sing(solfa[6], speed=400)
    def GGGGGG():
        display.show(Image.SURPRISE)
        sing(solfa[6], speed=400)
    def GGGGGGGG():
        display.show(Image.SURPRISE)
        sing(solfa[6], speed=400)
    def shake():
        display.show(Image.SURPRISE)
        sing(solfa[6], speed=400)
    dance = {
        'up':up,
        'down':down,
        'right':right,
        'left':left,
        'face up':face_up,
        'face down':face_down,
        'freefall':freefall,
        '3g':GGG,
        '6g':GGGGGG,
        '8g':GGGGGGGG,
        'shake':shake}