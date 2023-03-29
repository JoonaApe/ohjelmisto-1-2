'''
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
'''
from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user='user1',
    password='sala1',
    autocommit=True)

app = Flask(__name__)
@app.route('/kentta/<icao>')
def icaohaku(icao):
    try:
        icao = str(icao)
        sql = "SELECT name, municipality " +\
        f"FROM airport WHERE ident = '{icao}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount == 0:
            raise ValueError()
        name = tulos[0][0]
        muni = tulos [0][1]

        tilakoodi = 200
        vastaus = {
            "status" : tilakoodi,
            "ICAO" : icao,
            "Name" : name,
            "Municipality" : muni
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status" : tilakoodi,
            "teksti" : "Virheellinen icao koodi"
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