'''
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.

Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
 joka kysytään käyttäjältä ohjelman suorituksen alussa.
'''
import random

def nopat(tahkot):
    x = random.randint(1,tahkot)
    return x
numerot = int(input('Anna tahkojen määrä. '))

game_on = True
while game_on:
    print(nopat(numerot))
    if numerot == nopat(numerot):
        print(f'{numerot} Sait nopan suurimman numeron!')
        game_on = False

