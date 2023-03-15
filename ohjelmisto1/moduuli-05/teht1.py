'''
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
'''
import random

kuutiot = int(input('Kuinka monta arpakuutiota heitetään? '))
summa = 0
for i in range(kuutiot):
    heitto = random.randint(1,6)
    summa += heitto
print(f'Heitit {kuutiot} arpakuutiota ja niiden summa on {summa}')




