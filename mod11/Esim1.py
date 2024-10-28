class Koira():
    def __init__(self, nimi, tervehdys="hau, hau!"):
        self.nimi = nimi
        self.tervehdys = tervehdys

    def tervehdi(self):
        print(self.tervehdys)

class RotuKoira(Koira):
    def __init__(self, nimi, rotu, tervehdys="hau, hau!"):
        super().__init__(nimi, tervehdys)
        self.rotu = rotu

    def tervehdi(self):
        # ylikirjoitetaan yliluokalta peritty metodi
        print(f"{self.tervehdys}, rotuni on {self.rotu}")

koiraA = Koira("Ressu")
hieno_koira = RotuKoira("Mr Bean", "beagle", "Vuh, vuh")

koiraA.tervehdi()
hieno_koira.tervehdi()

