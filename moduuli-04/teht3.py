''' 3. Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
'''
suurin = None
pienin = None

while True:
    luvut = input('Anna numeroita: ')
    if not luvut:
        break
    luvut = int(luvut)

    if suurin is None:
              suurin = luvut
    elif luvut > suurin:
        suurin = luvut
    if pienin is None:
        pienin = luvut
    elif luvut < pienin:
        pienin = luvut

print(f'Suurin: {suurin}\nPienin: {pienin}')






