'''
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
helikopterikenttiä on 15 kappaletta jne.
'''
import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user='user1',
    password='sala1',
    autocommit=True)

def tuloste():
    sql1 = "SELECT  type, COUNT(*) as count " +\
        f"FROM airport WHERE iso_country = '{maatunnus}'" +\
        "GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql1)
    tulos = kursori.fetchall()
    if kursori.rowcount >= 1:
        for i in tulos:
            print(i[0],i[1])


maatunnus = input('Anna maatunnus: ')
tuloste()