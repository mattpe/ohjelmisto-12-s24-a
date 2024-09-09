'''
Joukko (set)
- alkiot aaltosulkujen { } sisällä
- vrt korttipakka:
   - kukin pakan kortti on erilainen kuin muut
   - pakassa ei saa olla kahta samanlaista korttia
- alkioiden järjestystä joukkossa ei ole määritelty
  -> tulostusjärjestystä ei voi tietää
  -> alkioilla ei ole indeksiä
- joukkoon voi yrittää  lisätä saman alkion toiseen
  kertaan -> ei virhettä, muttaa alkiota ei lisätä joukkoon.

Tyhjän joukon luonti poikkeaa muista rakenteista
tyhja_joukko = set()
'''

# luodaan tyhjä joukko numeroita varten, huomaa poikkeava tapa
numerot = set()

# boolean-muuttuja (True/False), jonka mukaan toistoa jatketaan
jatketaan = True    # alkuarvo = toistoa jatketaan
# käyttäjän antama luku otetaan tähän talteen
luku = 0

print("Kysyn sinulta numeroita, kunnes annat jonkin luvun uudelleen")

# while-toistossa jatketaan, kunnes jatketaan = False
while jatketaan:        # sama kuin while jatketaan == True:
    luku = int( input("Anna luku: ") )
    # tarkistetaan onko luku jo annettu
    if luku in numerot:
        # luku oli jo annettu, lopetetaan toisto
        jatketaan = False
        print(f"Olit jo antanaut luvun {luku}, lopetetaan")
    else:
        # uusi luku, lisätään se joukkoon
        numerot.add(luku)
        print("Numerosi lisättiin joukkoon")

# tulostetaan kaikki annetut luvut
print("Antamasi luvut satunnaisessa järjestyksessä:")
for arvo in numerot:
    print(arvo)
