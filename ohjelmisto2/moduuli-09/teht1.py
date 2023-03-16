'''
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
'''

class Auto:
    def __init__(self, rekkari, topSpeed , currentSpeed = 0, trip = 0):
        self.rekkari = rekkari
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.trip = trip

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto.rekkari}, Auton huippunopeus: {auto.topSpeed} km/h, Auton tämän hetkinen nopeus: {auto.currentSpeed} km/h, Kuljettu matka: {auto.trip} kilometriä")