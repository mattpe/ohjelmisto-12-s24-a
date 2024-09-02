import math # importit aina tiedoston alkuun
import random

# Kysytään käyttäjältä syöte (input)
# Ja sijoitetaaan käyttäjä syöttämä merkkijono (string) muuttujaan
name = input("Anna nimesi:")
# Tulostetaan muuttujan arvo (output)
print("Moi " + name)

# tallennetaan ikä kokonaislukuna (int)
#age = 6
# tai liukulukuna (float)
#age = 6.5

# luetaan ikä käyttäjältä, input palauttaa aina stringin
age = input("Anna ikä: ")
# muutetaan ikä kokonaisluvuksi
age = int(age)
print(age)
age_string = str(age) # 6 -> "6"
print("Moi " + name + " ikäsi on " + age_string)
# tai
print("Moi " + name + " ikäsi on " + str(age))
# lisätään ikään 1 vuosi
age = age + 1
print(f"Kahden vuoden päästä ikäsi on {age+1:16.3f}")

print(f"Piin likiarvo: {math.pi:.2f}")

# t2.

r = float(input("Anna ympyrän säde (m): ")) # esim. "4.5" -> 4.5
area = math.pi * r * r
area = round(area, 2) # pyöristys 2 desimaalin tarkkuuteen
print(f"Ympyrän pinta-ala on {area} neliömetriä.")

# t6. tip
random.randint(1, 6) # palattauttaa int-arvon väliltä 1-6
print(f"Noppa heitetty: {random.randint(1, 6)}")
