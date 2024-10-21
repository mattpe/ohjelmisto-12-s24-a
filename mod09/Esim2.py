'''
Laajennetaan edellisen esimerkin Kissa-luokkaa
'''

class Kissa:
    # luokkamuuttuja, kaikille luokan olioille yhteinen
    kissojenLkm = 0

    # määritellään luokan alustaja
    def __init__(self, nimi, age, tervehdys = "Miau, miau"):
        # tervehdys-parametria ei ole pakko antaa
        self.nimi = nimi
        self.ikä = age
        # määritellään myös kolmas ominaisuus
        self.omistaja = "Tuntematon"
        self.tervehdys = tervehdys
        # päivitetään luokkamuuttujan arvo
        Kissa.kissojenLkm += 1

    # määritellään oliolle toiminto eli metodi
    def tervehdi(self):
        print(self.tervehdys)


tokaKissa = Kissa("Mörri", 3, "MOOUU!!!")
kolmasKissa = Kissa("Mirri", 1)
# kutsutaan olioiden toimintoa
tokaKissa.tervehdi()
kolmasKissa.tervehdi()
# tulostan luokkamuuttujan arvon
print(f"Kissa-olioita on luotu {Kissa.kissojenLkm} kpl")
