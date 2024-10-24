"""
Kissa-luokka ja assosiaatiot
"""

class Kissa:
    # luokkamuuttuja, kaikille luokan olioille yhteinen
    kissojenLkm = 0

    # määritellään luokan alustaja
    def __init__(self, nimi, age, tervehdys = "Miau, miau", omistaja=None):
        # tervehdys-parametria ei ole pakko antaa
        self.nimi = nimi
        self.ika = age
        # omistaja on viittaus Omistaja luokasta luotuun olioon
        self.omistaja = omistaja
        # käytetään viittausta Omistaja-olioon, ja lisätään nyt luotava
        # Kissa-olio omistajan listalle (=> assosiaatio kahteen suuntaan)
        omistaja.lisaa_kissa(self)
        self.tervehdys = tervehdys
        # päivitetään luokkamuuttujan arvo
        Kissa.kissojenLkm += 1

    # määritellään oliolle toiminto eli metodi
    def tervehdi(self):
        print(f"{self.tervehdys}! olen {self.nimi}")
        print(f"Ikäni on {self.ika} vuotta.")
        print(f"Minut omistaa {self.omistaja.nimi}")

class Omistaja:
    def __init__(self, nimi, puh="tuntematon"):
        self.nimi = nimi
        self.puh = puh
        self.kissat = []

    def lisaa_kissa(self, kissa):
        # estetään saman kissan päätyminen listalle kahteen kertaan
        for k in self.kissat:
            if k == kissa:
                return
        self.kissat.append(kissa)

    def esittele(self):
        print(f"Olen {self.nimi}, puh: {self.puh}")
        print(f"Omistan kissat:")
        for k in self.kissat:
            print(f"{k.nimi}, ikä: {k.ika}")


# Luodaan omistaja tyyppinen olio
viivi = Omistaja("Viivi Virtanen")
# Sijoitetaan viittaus Omistaja-olioon kissa-olioiden ominaisuudeksi = assosiaatio
cat1 = Kissa("Mörri", 3, "MOOUU!!!", viivi)
# käytetään omistajalle nimetty parametria, koska tervehdys-parametri jää välistä
cat2 = Kissa("Mirri", 1, omistaja=viivi)
# kutsutaan olioiden toimintoa
cat1.tervehdi()
cat2.tervehdi()

# Kissa-luokka tekee alla olevan
#viivi.lisaa_kissa(cat1)
#viivi.lisaa_kissa(cat1)
#viivi.lisaa_kissa(cat2)

viivi.esittele()

# laitetaan kaikkin viivin kissat esittelemään itsensä
for kissa in viivi.kissat:
    kissa.tervehdi()

# luodaan 5 kissaa lisää ja lisätään viittaukset luotuihin olioihin listaan
"""
cats = []
for i in range(5):
    new_cat = Kissa(f"Cat name {i}", i, f"Moro {i}")
    cats.append(new_cat)
# kaikki uudet kissat tervehtii
for cat in cats:
    cat.tervehdi()
"""

# tulostan luokkamuuttujan arvon
print(f"---\nKissa-olioita on luotu {Kissa.kissojenLkm} kpl")
