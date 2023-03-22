'''
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
'''
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

class Sähköauto(Auto):
    def __init__(self, rekkari, topSpeed, akkukapasiteetti):
        super().__init__(rekkari,topSpeed)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottori(Auto):
    def __init__(self, rekkari, topSpeed, tankki):
        self.tankki = tankki
        super().__init__(rekkari,topSpeed)

tehosekoitin = Sähköauto("ABC-15",180, 52.5)
oikea_auto = Polttomoottori("ACD-123", 165, 32.3)

print(f"Sähköautolla ajettu {tehosekoitin.trip}")
print(f"Oikealla autolla ajettu {oikea_auto.trip}")
tehosekoitin.accelerate(120)
oikea_auto.accelerate(150)

tehosekoitin.drive(3)
oikea_auto.drive(3)

print(f"Sähköautolla ajettu  3 tunnin jälkeen {tehosekoitin.trip} kilometriä")
print(f"Oikealla autolla ajettu 3 tunnin jälkeen {oikea_auto.trip} kilometriä")

