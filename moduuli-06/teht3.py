'''
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
'''

def muunnos(gallonat):
    litra = gallonat * 3.7854
    return litra


while True :
    galtsut = int(input('Anna gallonat nii muutan ne litroiks: '))
    if galtsut < 0:
        print('Annoit negatiivisen luvun, se ei toimi >:(((((')
        break
    print(f'{galtsut} gallonaa on {muunnos(galtsut)} litraa')


