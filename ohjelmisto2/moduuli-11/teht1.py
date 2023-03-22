'''
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
'''

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivuLkm):
        self.kirjoittaja = kirjoittaja
        self.sivuLkm = sivuLkm
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Sivujen lukumäärä:{self.sivuLkm}, Kirjoittaja:{self.kirjoittaja}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja, ):
        self.paatoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")

lehti = Lehti("Aku Ankka","Aki Hyyppä")
kirja = Kirja("Hytti n:6","Rosa Liksom", 200)
lehti.tulosta_tiedot()
kirja.tulosta_tiedot()

