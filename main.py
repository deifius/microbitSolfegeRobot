from solfege import pronounce, sing, solfa, ahem, sing_up, sing_down
from dances import dances
from microbit import sleep, Image, button_a, button_b, display, accelerometer

"""
I am a little robot that sings as you dance with me
hold me in your hand and turn me around
I can remember the song if you remember the hand dance
"""

def main():
    display.show(Image.SURPRISED)
    ahem()
    sleep(1000)
    gesture = ''
    moves = dances.dance
    while True:
        last_gesture = gesture
        gesture = accelerometer.current_gesture()
        if gesture in ['up','down','left','right','face up','face down']:
            if last_gesture != gesture:
                moves[gesture]()
        if button_a.is_pressed():
            display.show(Image.HAPPY)
            sing_up()
        elif button_b.is_pressed():
            display.show(Image.SURPRISED)
            sing_down()
        else:
            display.show(Image.ASLEEP)

    display.clear()

if __name__ == "__main__": main()