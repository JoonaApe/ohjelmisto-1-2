'''
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
'''

from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<num>')
def alkuluku(num):
    try:
        num = int(num)
        isPrime = True
        if num == 1:
            isPrime = False
        elif num > 1:
            for i in range(2, num):
                if num % i == 0:
                    isPrime = False
                    break
        else:
            isPrime = True

        tilakoodi = 200
        vastaus = {
            "status" : tilakoodi,
            "Number" : num,
            "isPrime" : isPrime
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status" : tilakoodi,
            "teksti" : "Virheellinen yhteenlaskettava"
        }
    jsonvastaus = json.dumps(vastaus)
    return Response(response=jsonvastaus, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvastaus = json.dumps(vastaus)
    return Response(response=jsonvastaus,status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)