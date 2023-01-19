''' Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
 Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
 Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
 Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
'''

import random
luku = random.randint(1,10)

while True:
    vastaus = input('Arvaa luku väliltä 1 ja 10: ')
    vastaus = int(vastaus)
    if vastaus == luku:
        print('Oikein!!')
        break


    if vastaus < luku:
        print('Liian pieni arvaus!')
    elif vastaus > luku:
        print('Liian suuri arvaus!')
