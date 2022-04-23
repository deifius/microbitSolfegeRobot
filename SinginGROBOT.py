from solfege import pronounce, sing, solfa
from microbit import sleep, Image, button_a, button_b, display, accelerometer

"""
I am a little robot that sings as you dance with me
hold me in your hand and turn me around
I can remember the song if you remember the hand dance
"""


def ahem():
    # Clearing the throat requires the use of phonemes. Changing
    # the pitch and speed also helps create the right effect.
    pronounce("AEAE/HAEMM", pitch=200, speed=100)  # Ahem
    sleep(1000)

def main():
    ahem()
    while True:
        gesture = 'nothing yet'
        last_gesture = gesture
        gesture = accelerometer.current_gesture()
        if last_gesture != gesture:
            if gesture == "down":
                display.show(Image.CLOCK6)
                sing(solfa[1], speed=100)
                #sleep(1000)
            if gesture == "right":
                display.show(Image.CLOCK9)
                sing(solfa[2], speed=100)
                #sleep(1000)
            if gesture == "left":
                display.show(Image.CLOCK3)
                sing(solfa[4], speed=100)
                #sleep(1000)
            if gesture == "face up":
                display.show(Image.CLOCK1)
                sing(solfa[5], speed=100)
                #sleep(1000)
            if gesture == "face down":
                display.show(Image.CLOCK7)
                sing(solfa[6], speed=100)
                #sleep(1000)
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