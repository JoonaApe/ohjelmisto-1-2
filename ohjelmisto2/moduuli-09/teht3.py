'''
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
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

auto = Auto("ABC-123", 142, 0, 2000)
print(f"Autolla kuljettu: {auto.trip} kilometriä")
auto.accelerate(60)
auto.drive(1.5)
print(f"Autolla kuljettu: {auto.trip} kilometriä.")