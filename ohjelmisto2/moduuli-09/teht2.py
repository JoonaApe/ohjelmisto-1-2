'''
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.
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
auto = Auto("ABC-123", 142)

auto.accelerate(30)
auto.accelerate(70)
auto.accelerate(50)
print(f"Auton tämän hetkinen nopeus: {auto.currentSpeed} km/h")
auto.accelerate(-200)

print(f"Auton tämän hetkinen nopeus: {auto.currentSpeed} km/h")
