import json
from flask import Flask, request, Response

app = Flask(__name__)

# dummy eka testi
# pyyntö: GET http://127.0.0.1:3000/joku-juttu
@app.route('/joku-juttu')
def print_joku_juttu():
    return 'Siinä sulle joku kolmas juttu!'

# pyyntö esim: GET http://127.0.0.1:3000/sum?num1=3&num2=3.4
@app.route('/sum')
def calculate_sum():
    # print(request.args.get('num2'))
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except ValueError:
        return 'Parameter error: use numbers!'
    except TypeError:
        return 'Parameter(s) missing!'
    return {
        "function": "calculate sum of two values",
        "result": num1 + num2
    }

# "mock data" eli ns. testidataa
names = ['Aku', 'Iines', 'Hannu', 'Heluna']

# pyyntö: GET http://127.0.0.1:3000/names
# lähetetään kaikki nimet json-muodossa
@app.route('/names')
def get_names():
    return {"names": names}

# pyyntö esim: GET http://127.0.0.1:3000/names/3
# haetaan yksi nimi listalta perustuen indeksiin ("id")
@app.route('/names/<id>')
def get_name(id):
    try:
        result = {"id": id, "name": names[int(id)]}
    except IndexError:
        # status-koodin vaihtaminen vaatii oman response-olion luonnin
        res_body = {"error": "not found"}
        # muutetaan sanakirja -> json-muotoinen merkkijono
        res_body = json.dumps(res_body)
        response = Response(status=404, response=res_body,
                            content_type="application/json")
        return response
    return result

# yleinen virheenkäsittely 404 virheille
@app.errorhandler(404)
def not_found(error):
    #print(error)
    #print(request.path)
    res_body = {"route": request.path,
                "error": "not found"}
    # muutetaan sanakirja -> json-muotoinen merkkijono
    res_body = json.dumps(res_body)
    response = Response(status=404, response=res_body,
                        content_type="application/json")
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)
