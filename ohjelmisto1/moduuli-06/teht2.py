'''
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.

Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
 joka kysytään käyttäjältä ohjelman suorituksen alussa.
'''
import random

def nopat(tahkot):
    return random.randint(1,tahkot)


numerot = int(input('Anna tahkojen määrä. '))
while True:
        luku = nopat(numerot)
        print(f'nopasta tuli: {luku}')
        if numerot == luku:
            print(f'\nSait nopan suurimman numeron!')
            break