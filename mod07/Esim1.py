"""
Monikko (tuple) on lähes kuin lista.
- vakio, monikon luonnin jälkeen sen alkioita ei
voi muokata.
- alkiot laitetaan kaarisulkujen ( ) sisään (suositus)
- monikon avulla funktio voi käytännössä palauttaa
  useita arvoja (1 kpl monikkoja).
"""

# luodaan monikko sallituista väreistä (RGB)
varit = ("punainen", "vihreä", "sininen")

# kysytään käyttäjältä arvaus
arvaus = input("Arvaa väri joka on minun monikossa: ")

# onko arvattu väri monikossa?
if arvaus in varit:
    # kuinka mones alkio väri oli monikossa?
    nro = varit.index(arvaus)

    print(f"Osuit, {arvaus} on {nro+1}. väri monikossa")
else:
    print("Väri ei löytynyt monikosta")
