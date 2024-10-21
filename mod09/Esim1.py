'''
Määritellään Kissa-luokka.
Luokalla on kolme ominaisuutta.
'''

class Kissa:
    # määritellään luokan alustaja
    def __init__(self, nimi, age):
        self.nimi = nimi
        self.ikä = age
        # määritellään myös kolams ominaisuus
        self.omistaja = "Tuntematon"


# pääohjelma
# luodaan uusi Kissa-tyyppinen olio
ekaKissa = Kissa("Pörri", 3)
# tulostetaan kisan arvoja
print(f"Kissan nimi on {ekaKissa.nimi}")


