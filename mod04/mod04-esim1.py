# Moduuli 4 - while esimerkkejä
"""
while True:
    print("Ikuinen silmukka, ei saa tapahtua!")
"""
import random

"""
hooray_count = int(input("Kuinka monta kertaa hurrataan? "))
hooray_counter = 0
while hooray_counter < hooray_count: # ehdosta syntyy aina True tai False
    # tulostetaan ehdosta syntyvä arvo
    # print(hooray_counter < 3)
    hooray_counter = hooray_counter + 1 # hooray_counter += 1
    print(f"{hooray_counter}. kerran Hurraa!")
print(f"Hurrattiin {hooray_counter} kertaa.")
"""

# noppapeli

rounds = 0
total_throw_count = 0
while rounds < 10000:
    rounds += 1
    die1 = die2 = counter = 0
    while die1 != 6 or die2 != 6:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        counter += 1
        #print(f"Noppien silmäluvut: {die1}, {die2}, heittojen lkm: {counter}")
    total_throw_count = total_throw_count + counter
    #print(f"Heittojen lkm tällä kierroksella: {counter}, yhteensä: {total_throw_count}")
print(f"Heittojen lkm keskiarvo: {total_throw_count/rounds}")

# sisäkkäiset while-silmukat
eka = 1
while eka <= 5:
    print("Ulompi silmukka alkaa")
    toka = 1
    while toka <= 5:
        print("Sisempi silmukka alkaa")
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1

# "komentorivikäyttöliittymä"
command = ""
while command != "lopeta":
    command = input("Anna komento> ")
    if command == "tulosta":
        print("Tulostetaan")
    elif command == "hurraa":
        hooray_count = int(input("Kuinka monta kertaa hurrataan? "))
        hooray_counter = 0
        while hooray_counter < hooray_count:  # ehdosta syntyy aina True tai False
            hooray_counter = hooray_counter + 1  # hooray_counter += 1
            print(f"{hooray_counter}. kerran Hurraa!")
        print(f"Hurrattiin {hooray_counter} kertaa.")
    elif command == "noppa":
        die1 = die2 = counter = 0
        while die1 != 6 or die2 != 6:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            counter += 1
            # print(f"Noppien silmäluvut: {die1}, {die2}, heittojen lkm: {counter}")
        print(f"Heittojen lkm: {counter}")
    elif command == "lopeta":
        print("Lopetetaan ohjelma")
        #break # toistorakenteen suoritus loppuu heti.
    else:
        print("En ymmärrä. Tarkista komentosi, kiitos.")
print("Ohjelman suoritus loppui.")



