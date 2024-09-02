# Piin likiarvon laskeminen
# π≈4n/N, jossa n on yksikköympyrän sisälle osuvat pisteet, N on kaikki pisteet
# epäyhtälöllä x^2+y^2<1 testataan, onko yksittäinen piste ympyrän sisällä

#toinen tapa importata vain yksittäisiä toimintoja/funktioita
#from random import randint
#randint(-1, 1)

import math
import random
iterator = 0
#TODO: Kysy N arvo käyttäjältä
N = 100000 # pisteiden kokonaismäärä
n = 0 # ympyrään sisään osuvat pisteet
while iterator < N:
    iterator += 1
    # arvotaan koordinaatit liukulukuina väliltä -1 ja 1, kaksi erilaista tapaa:
    x = random.random() * 2 - 1
    y = random.uniform(-1, 1)
    #print(f"Satunnainen piste: {x}, {y}")
    #print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Osui ympyrän sisälle.")
        n = n + 1
print(f"{N} pisteestä {n} osui yksikköympyrän sisälle.")
result = 4 * n / N
print(f"Piin likiarvo on {result}")
print (f"Virhe verrattuna math.pi ({math.pi:.5f}): {result - math.pi:.5f}")
