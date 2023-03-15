import random


def calculateSum(number1,number2):
    result = number1 + number2
    return result

#print(calculateSum(11,34))


correct_int = random.randint(1,10)
def checkGuess(guess):
    if guess < correct_int:
        return 'Liian pieni'
    elif guess > correct_int:
        return 'Liian suuri'
    else:
        return 'Oikein!'

def guessGame():
    game_on = True
    while game_on:
        arvaus = int(input('arvaa luku '))
        print(checkGuess(arvaus))
        if checkGuess(arvaus) == 'Oikein!':
            game_on = False


viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")


import random

def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return eka, toka

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")


pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

for o in pelit:
    print(o)

