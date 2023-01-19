'''
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).
'''

kt = 'python'
ss = 'rules'
yritykset = 0


while yritykset < 5:
    kt1 = input('Anna käyttäjätunnus: ')
    ss1 = input('Anna salasana: ')
    if kt1 == kt and ss1 == ss:
        print('Tervetuloa!')
        break

    elif kt1 != kt or ss1 != ss:
        print(f'Väärin!\n')
        yritykset += 1
    if yritykset >= 5:
        print('Pääsy evätty! Syötit tiedot liian useasti väärin.')
