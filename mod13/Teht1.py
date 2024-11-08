"""
    Alla on perusratkaisu.
    Ei sisällä varautumista poikkeuksiin jne.
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def onkoAlkuluku(luku):
    onAlku = True       # alkuoletus: saatu luku on alkuluku

    if luku < 2:
        onAlku = False

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            # luku oli jaollinen muulla kuin 1 tai itsellään
            # -> EI ole alkuluku
            onAlku = False
            break

    # tulostetaan saadut vastaukset web-sivulle
    vastaus = {
        "Number" : luku,
        "isPrime" : onAlku
    }

    # palautetaan vastaus web-sivulle
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
