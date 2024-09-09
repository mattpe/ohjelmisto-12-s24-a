'''
Esimerkkejä ehtolauseista
'''

ika = int( input("Anna ikäsi: ") )

# ns. joko-tai rakenne
if ika >= 18:
    # Tämä on ns. if-ehdon lohko (block)
    # Tänne tullaan, jos ehto on totta, eli
    # ika on suurempi tai yhtäsuuri kuin 18
    print("Tervetuloa bileisiin!")
else:
    # tänne tullaan, jos ehto ei ole totta
    print("Go home, Baby!")

print("Ohjelma loppui")
