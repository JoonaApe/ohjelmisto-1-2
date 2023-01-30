'''
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.

'''
nimet = set()


while True:
    nimi = input('Anna nimiä tai lopeta painamalla Enter. ')
    if nimi == "":
        break

    elif nimi in nimet:
        print("aiemmin syötetty")
    else:
        print("uusi nimi")
        nimet.add(nimi)
print('Nimet: ')

for nimi in nimet:
    print(nimi)
