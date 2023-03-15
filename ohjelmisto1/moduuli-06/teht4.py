'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

'''
def summa(lista):
    return sum(lista)



numerot = [10,12,23,512,22,31,2,413]
print(numerot)
print(f'Yllä olevien numeroiden summa: {summa(numerot)}')
