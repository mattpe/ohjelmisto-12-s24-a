'''
Sanakirja
- alkiot aaltosulkujen { } sisällä
- yksi alkio koostuu avain-arvo parista 'avain': 'arvo'
'''

# Oma puhelinluettelo

# funktio/aliohjelma tulostaa puhelinluettelon kaikki arvot
def tulosta_luettelo():
    print("Puhelinluettelon sisältö:")
    for avain in puhelinNumerot:
        print(f"{avain} : {puhelinNumerot[avain]}")
    return

# funktio lisää uuden yhteystiedon sanakirjaan
def lisaa_kayttaja():
    # kysytään tarvittavat tiedot
    nimi = input("Anna uuden kaverin nimi: ")       # avain
    numero = input("Puhelinnumero: ")               # arvo
    # lisätään uusi tieto sanakirjaan
    puhelinNumerot[nimi] = numero


# -- pääohjelma alkaa --

# tehdään tyhjä sanakirja puhelinluetteloa varten
puhelinNumerot = { }

# Ohje käyttäjälle
print("\n1 = numeron haku nimellä, 2 = numeron lisäys, "
      "3 = tulosta kaikki tiedot, 9 = lopetus")
# kysytään käyttäjältä toiminto
toiminto = int( input("Valitse toiminto: "))

# tässä pyöritään, kunnes käyttäjä lopettaa
while toiminto != 9:
    if toiminto == 1:
        print("Toiminto on tulosa...")
    elif toiminto == 2:
        lisaa_kayttaja()
    elif toiminto == 3:
        tulosta_luettelo()
    else:
        print("Tuntematon komento")

    # Ohje käyttäjälle
    print("\n1 = numeron haku nimellä, 2 = numeron lisäys, 3 = tulosta kaikki tiedot, 9 = lopetus")
    # kysytään käyttäjältä toiminto
    toiminto = int(input("Valitse toiminto: "))

print("Hyvää päivän jatkoa!")