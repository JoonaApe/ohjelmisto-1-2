import mysql.connector


yhteys = mysql.connector.connect(
         host='localhost',  #oma kone
         port= 3306,        #verkko portti
         database='flight_game',    #tietokannan nimi
         user='user1',      #tietokannan käyttäjä
         password='sala1',  #salasana
         autocommit=True    #muutokset tallnnetaaan heti
         )


#funktio hakee ja tulostaa icao koodin mukaan lentoaseman.
def tulosta():
    sql = "SELECT name, municipality " +\
        f"FROM airport WHERE ident = '{icao}'"

    kursori = yhteys.cursor()

    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >= 1:
        for rivi in tulos:
            print(f'Lentokentän nimi: {rivi[0]}\nSijaintikunta: {rivi[1]}' )


#pääohjelma
icao = input('Anna lentokentän ICAO-koodi: ')
tulosta()



