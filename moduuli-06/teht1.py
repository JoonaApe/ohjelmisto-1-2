'''
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
'''
import random

def nopat():
   x = random.randint(1,6)
   return x


nopanheitto = nopat()
while nopanheitto != 6:
    print(nopanheitto)
    nopanheitto = nopat()

print(f'{nopanheitto}!!')






