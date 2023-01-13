"""
Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
"""

i = 1000
x = 1

while (x != i):
        if (x % 3 == 0):
                print(x)
        x += 1

