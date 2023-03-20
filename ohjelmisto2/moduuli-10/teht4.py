'''
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.

- Luokassa on seuraavat metodit:

- tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

- tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
kun kilpailu on päättynyt.
'''

import random
from prettytable import PrettyTable

class Auto:
    def __init__(self, rekkari, topSpeed , currentSpeed = 0, trip = 0):
        self.rekkari = rekkari
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.trip = trip
    def accelerate(self, speedDifference):
        self.currentSpeed = self.currentSpeed + speedDifference
        if self.currentSpeed > self.topSpeed:
            self.currentSpeed = self.topSpeed
        if self.currentSpeed < 0:
            self.currentSpeed = 0
    def drive(self, hours):
        self.trip = self.trip + (hours * self.currentSpeed)
class Kilpailu:
    def __init__(self, nimi, distance_km, num):
        self.nimi = nimi
        self.distance_km = distance_km
        self.lista = []
        for i in range(1,num+1):
            auto = Auto("ABC-" + str(i), random.randint(100,200))
            self.lista.append(auto)

    def tunti_kuluu(self):
        for auto in self.lista:
            auto.accelerate(random.randint(-10,15))
            auto.drive(1)
    def tulosta_tilanne(self):
        for auto in self.lista:
            print(f"{auto.rekkari}, Huippunopeus: {auto.topSpeed} km/h, Nopeus: {auto.currentSpeed} km/h, Kokonaismatka: {auto.trip} kilometriä")

    def kilpailu_ohi(self):
        for auto in self.lista:
            if auto.trip >= self.distance_km:
                auto.rekkari = auto.rekkari + "(W)"
                return True
        return False




kisa = Kilpailu("Suuri romuralli",8000,10)
print(f"Nyt alkaa {kisa.nimi}!")
aika = 0
while kisa.kilpailu_ohi() == False:
    aika += 1
    kisa.tunti_kuluu()
    if aika % 10 == 0:
        print(f"\nKilpailu on kestänyt {aika} tuntia.\n")
        kisa.tulosta_tilanne()
print(f"\n{kisa.nimi} on päättynyt!\nKilpailu kesti {aika} tuntia.\n")
kisa.tulosta_tilanne()


