class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin     # kerros missä hissi on

    def siirry_kerros(self, tavoite):
        # tarkistetaan että tavoite on salitulla välillä
        if tavoite >= self.ylin or tavoite < self.alin:
            print("Kerrosta ei ole olemassa!")
            return
        if self.kerros < tavoite:
            while self.kerros < tavoite:
                self.kerros_ylos()
        print(f"-- Hissi on halutussa kerroksessa -- \n")

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.hissit = []        # lista talon hisseistä
        self.luo_hissit(lkm)

    def luo_hissit(self, lkm):
        for nro in range(lkm):
            uusi_hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(uusi_hissi)
        return

    def aja_hissiä(self, hissin_nro, tavoitekerros):
        ajettava_hissi = self.hissit[hissin_nro - 1]
        ajettava_hissi.siirry_kerros(tavoitekerros)


taloA = Talo(1, 7, 3)
taloA.aja_hissiä(1, 5)
taloA.aja_hissiä(2, 10)
taloA.aja_hissiä(3, 2)


