'''
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
'''

num = int(input('Anna kokonaisluku niin kerron onko se alkuluku. '))
if num == 1:
        print('Antamasi luku ei ole alkuluku.')
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} ei ole alkuluku.')
            break
    else:
        print(f'{num} on alkuluku.')
