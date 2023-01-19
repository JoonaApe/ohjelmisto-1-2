"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
 Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""
while True:
    inch = float(input('Syötä mitta tuumana niin muutan ne senttimetreiksi '))
    if inch < 0:
        break
    cm = inch * 2.54
    print(f'{inch} tuumaa on {cm} senttimetriä')

