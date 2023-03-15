'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
'''

# funktio lisää uuden aseman sanakirjaan.

def lisaa():
    tunnus = input('Anna lentoaseman tunnus: ')
    nimi = input('Anna lentoaseman nimi: ')
    lentoasemat[tunnus] = nimi
    print('Asema on lisätty!')

#funktio tulostaa sanakirjassa olevat asemat.
def tulosta():
    print(lentoasemat)
    return

#funktio hakee lentoaseman icao tunnuksen perusteella.
def hae():
    tunnus = input('Anna haettavan aseman tunnus: ')
    if tunnus in lentoasemat:
        print(f'Lentoaseman nimi: {lentoasemat[tunnus]}')
    else:
        print('Lentoasemaa ei löydy.')
    return

lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema", "EFFS" : "Oulun lentoasema"}
while True:
    valinta = int(input('0 = Tulosta lentoasemien tiedot.\n1 = Lisää uusi asema.\n2 = Hae lentoasema.\n3 = Lopeta. '))
    if valinta == 0:
        tulosta()
    if valinta == 1:
        lisaa()
    elif valinta == 2:
        hae()
    elif valinta == 3:
        break

