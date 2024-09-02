'''
Luku on alkuluku, jos se on jaollinen vain 1 ja itsellään.

HUOM: älä pelkästään kopsaa tätä vastausta.
Katso vastauksen idea ja yritä koodata itse vastaava ratkaisu.
'''

# boolean-tyyppinen muuttuja (True/False),
# alkuoletuksena on että tutkittava luku ON alkuluku.
onAlkuluku = True

# kysy käyttäjältä tutkittava luku
tutkittava = int( input("Anna tutkittava luku: ") )

# Idea: jaan tutkittavan luvun 2, 3, 4, ...
# (tutkittava luku -1)
# Jos tutkittava luku on jaollinen yhdelläkin
# jakajalla, niin tutkittava luku EI ole alkuluku.

for jakaja in range(2, tutkittava):
    # jakaja saa arvot 2, 3, ... (tutkittava -1)
    if tutkittava % jakaja == 0:
        # tänne tullaan, jos jakolasku meni tasan
        # -> tutkittava luku ei ollut alkuluku
        onAlkuluku = False

        # lopetetaan for-toisto, koska lopputulos on
        # jo selvillä
        break       # lopettaa heti for-toiston

# tulostetaan käyttäjälle vastaus
if onAlkuluku:
    # edellä oleva on lyhennys: if onAlkuluku == True
    print("Tutkittava lukusi ON alkuluku")
else:
    print("Tutkittava lukusi EI ollut alkuluku")
