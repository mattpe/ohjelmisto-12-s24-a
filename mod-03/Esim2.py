'''
Monivalinta eli if-elif-else rakenne.
Korkeintaan yksi haaroista suoritetaan,
ts. käyttäjä saa vain yhden ilmoituksen.
'''

arvosana = int( input("Anna arvosanasi: "))

if arvosana == 5:
    print("Erinomaista!")
elif arvosana >= 3:
    print("Hyvä suoritus")
elif arvosana >= 1:
    print("Yritä parantaa jatkossa")
else:
    # tänne tullaan vain, jos mikään eo. ehto
    # ei ole toteutunut
    print("Hylätty, yritä uudelleen!")

