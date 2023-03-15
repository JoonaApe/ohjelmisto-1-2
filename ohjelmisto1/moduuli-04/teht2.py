"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
 Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""
while True:
    tuuma = float(input('Syötä mitta tuumana niin muutan ne senttimetreiksi '))
    if tuuma < 0:
        break
    cm = tuuma * 2.54
    print(f'{tuuma} tuumaa on {cm} senttimetriä')

