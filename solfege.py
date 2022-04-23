from speech import pronounce, sing

"""
I am syllable to pitch relations 
"""

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

#fegio = f'#{note}{syllable}'
up = ''.join(solfa)# Sing the scale ascending in pitch.
def sing_up():
    sing(up, speed=50)
solfa.reverse()
down = ''.join(solfa)
def sing_down():
    sing(down, speed=50)
    


def ahem():
    # Clearing the throat requires the use of phonemes. Changing
    # the pitch and speed also helps create the right effect.
    pronounce("AEAE/HAEMM", pitch=200, speed=100)  # Ahem
    sleep(1000)
