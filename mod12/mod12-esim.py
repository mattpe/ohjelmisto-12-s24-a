import requests

def search_show(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    # Jos verkko-operaatio ei onnistu, käsitellään poikkeustilanne
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkko-ongelma.")
        # print(e) # muuttuja, jossa viittaus Exception-olioon
        return

    # Jos palvelimelta tulee joku virhekoodi, lopetetaan funktio samantien
    if response.status_code != 200:
        print(f"Pyyntö ei onnistunut, status: {response.status_code}")
        return
    # parsitaan response bodyn (vastauksen runko) json formaatista Pythonin
    # vastaava tietorakenne (listoja ja sanakirjoja sisäkkäin)
    response_body = response.json()

    # Tulostetaan ensimmäinen hakutulos
    #print(f"Ohjelman nimi: {response_body[0]['show']['name']}")

    if len(response_body) < 1:
        print("ei tuloksia.")
        return

    # Tulostetaan kaikkien ohjelmien tietoja iteroimalla
    for item in response_body:
        print("---")
        print(item['show']['name'])
        print(f"Linkki: {item['show']['url']}")
        # genret on tallennettu listana sanakirjan sisään
        for genre in item['show']['genres']:
            print(genre)

#search_show("Emmerdale")
search_show(input("Anna hakusana: "))