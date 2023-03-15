import random

class Auto:
    def __init__(self, rekkari, topSpeed , currentSpeed = 0, trip = 0):
        self.rekkari = rekkari
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.trip = trip
    def accelerate(self, speedDifference):
        auto.currentSpeed = auto.currentSpeed + speedDifference
        if auto.currentSpeed > auto.topSpeed:
            auto.currentSpeed = auto.topSpeed
        if auto.currentSpeed < 0:
            auto.currentSpeed = 0
    def drive(self, hours):
        auto.trip = auto.trip + (hours * auto.currentSpeed)


autot = []
for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100,200))
    autot.append(auto)



auto = Auto("ABC-123", 142)

auto.accelerate(30)
auto.accelerate(70)
auto.accelerate(50)
auto.accelerate(-200)
auto.accelerate(60)
auto.drive(1.5)




#print(f"Auton rekisteritunnus: {auto.rekkari}, Auton huippunopeus: {auto.topSpeed} km/h, Auton tämän hetkinen nopeus: {auto.currentSpeed} km/h, Kuljettu matka: {auto.trip} kilometriä")

while True:
    for auto in autot:
        auto.accelerate(random.randint(-10,15))
        auto.drive(1)
        if auto.trip >= 1000:
            auto.rekkari = auto.rekkari + " (VOITTAJA!) "
            break
    else:
        continue
    break


for auto in autot:
    print(f"{auto.rekkari}, {auto.topSpeed} km/h, {auto.currentSpeed} km/h, {auto.trip} kilometriä")








