"""
Kysytään käyttäjältä nimet ja lisätään ne listaan.
Muokataan listan sisältöä.
"""

# luon tyhjän listan nimiä varten
nimet = []

# kysyn käyttäjältä osallistujien lukumäärän
lkm = int( input("Kuinka monta osallistujaa? ") )

# toistetaan nimien kysyminen tarvittava määrä
for i in range(lkm):
    nimi = input("Anna nimi: ")
    # lisätään saatu nimi listan loppuun (append)
    nimet.append(nimi)

# järjestetään nimet aakkosjärjestykseen
nimet.sort()

print("Nimet aakkosjärjestyksessä:")
print(nimet)

# muokataan listan alkioiden sisältöjä
nimet[1] = "Toka"   # huom indeksin numero
nimet[-1] = "Vika"
nimet.insert(0, "Uusi eka")

# tulostetaan listan alkiot kukin omalla rivillään (for.. in)
for alkio in nimet:     # muuttujan nimen (nyt: alkio) saa keksiä vapaasti
    print(alkio)

