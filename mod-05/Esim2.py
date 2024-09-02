"""
range-funktio ja for-toisto
"""

print("Tulostan parilliset luvut väliltä 10 ... 20")

for nro in range(10, 21, 2):
    # huom: alkuarvo 10 kuuluu tarkasteltavaan väliin,
    # mutta loppuarvo 21 EI kuulu.
    # Kolmas parametri (nyt 2) kertoo lisäyksen määrän
    print(nro)

print("Tulostan kaikki luvut väliltä 5 ... 10")

for nro in range(5, 11):
    # lisäyksen oletusarvo on 1
    print(nro)

# Tervehditään 5 kertaa
for nro in range(5):
    # nro saa arvot 0, 1, .., 4
    print(f"Hei {nro + 1}. kerran")
