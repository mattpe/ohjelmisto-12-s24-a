# mod 10 teht 1
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin or kohde_kerros < self.alin:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa.")
            return
        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros == self.ylin:
            print("Ylin kerros jo saavutettu.")
            return
        self.nykyinen_kerros += 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros == self.alin:
            print("Alin kerros jo saavutettu.")
            return
        self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

hissi = Hissi(1, 9)
hissi.siirry_kerrokseen(89)
hissi.siirry_kerrokseen(7)
hissi.siirry_kerrokseen(6)
hissi.siirry_kerrokseen(2)
hissi.siirry_kerrokseen(9)
hissi.kerros_ylos()