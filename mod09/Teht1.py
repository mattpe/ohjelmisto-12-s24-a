# Määritellään Auto-luokka
class Auto:
    def __init__(self, rekkari, max):
        self.rekisteritunnus = rekkari
        self.huippunopeus = max
        # seuraavat ominaisuudet asetetaan nolliksi
        self.nopeus = 0
        self.kuljettu_matka = 0


# pääohjelma
# luodaan Auto-tyyppinen olio
eka_auto = Auto("ABC-123", 142)

# tulostetaan olion kaikki ominaisuudet
print("Auto-olion ominaisuudet")
print(f"Rekkari: {eka_auto.rekisteritunnus}")
print(f"huippunopeus: {eka_auto.huippunopeus} km/h")
print(f"Tämän hetken nopeus: {eka_auto.nopeus} km/h")
print(f"Auton kulkeman matka {eka_auto.kuljettu_matka} km")


