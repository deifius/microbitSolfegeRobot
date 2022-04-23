from speech import pronounce, sing
from microbit import sleep, Image, button_a, button_b, display, accelerometer

# The say method attempts to convert English into phonemes.
#say("I can sing!")
#sleep(1000)
#say("Listen to me!")
#sleep(1000)

def ahem():
    # Clearing the throat requires the use of phonemes. Changing
    # the pitch and speed also helps create the right effect.
    pronounce("AEAE/HAEMM", pitch=200, speed=100)  # Ahem
    sleep(1000)

# Singing requires a phoneme with an annotated pitch for each syllable.
solfa = [
    "#115DOWWWWWW",   # Doh
    "#103REYYYYYY",   # Re
    "#94MIYYYYYY",    # Mi
    "#88FAOAOAOAOR",  # Fa
    "#78SOHWWWWW",    # Soh
    "#70LAOAOAOAOR",  # La
    "#62TIYYYYYY",    # Ti
    "#58DOWWWWWW",    # Doh
]

fegio = f'#{note}{syllable}'
up = ''.join(solfa)# Sing the scale ascending in pitch.
def sing_up():
    sing(up, speed=50)
solfa.reverse()
down = ''.join(solfa)
def sing_down():
    sing(down, speed=50)
gesture = 'nothing yet'

def main()
    ahem()
    while True:
        last_gesture = gesture
        gesture = accelerometer.current_gesture()
        if last_gesture != gesture:
            if gesture == "up":
                display.show(Image.CLOCK12)
                sing(solfa[0], speed=100)
                #sleep(1000)
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