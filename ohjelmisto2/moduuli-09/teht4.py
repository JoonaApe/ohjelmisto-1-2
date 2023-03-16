import random

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


autot = []
for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100,200))
    autot.append(auto)


while True:
    for auto in autot:
        auto.accelerate(random.randint(-10,15))
        auto.drive(1)
        if auto.trip >= 10000:
            auto.rekkari = auto.rekkari +" (VOITTAJA!)"
            break
    else:
        continue
    break


for auto in autot:
    print(f"{auto.rekkari}, {auto.topSpeed} km/h, {auto.currentSpeed} km/h, {auto.trip} kilometriä")








