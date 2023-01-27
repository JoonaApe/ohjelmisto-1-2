'''
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.

Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
'''
import math
def pizza_kone(halkaisija,hinta):
    r = halkaisija / 2
    pinta_ala = (math.pi * (r*r)) * 0.0001
    koko_hinta = hinta / pinta_ala
    return koko_hinta

halkaisija1= float(input('Anna pizzan halkasija: '))
hinta1 = float(input('Anna saman pizzan hinta: '))
yksikko_hinta1 = pizza_kone(halkaisija1,hinta1)

halkaisija2 = float(input('Anna toisen pizzan halkaisija: '))
hinta2 = float(input('Anna toisen pizzan hinta: '))
yksikko_hinta2 = pizza_kone(halkaisija2,hinta2)

if yksikko_hinta1 < yksikko_hinta2:
    print(f'Ensimmäinen pizza antaa paremman vastineen rahoille, sen hinta on {yksikko_hinta1:.2f} euroa per neliömetri, toisen pizzan hinta on {yksikko_hinta2:.2f} euroa per neliömetri')

elif yksikko_hinta1 > yksikko_hinta2:
    print(f'Toinen pizza antaa paremman vastineen rahoille, sen hinta on {yksikko_hinta2:.2f} euroa per neliö metri, ensimmäisen pizzan hinta on {yksikko_hinta1:.2f} euroa per neliömetri')
else:
    print('Pizzat ovat yhtä hyviä vastineita rahoille.')


