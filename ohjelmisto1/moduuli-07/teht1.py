'''
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
'''
vuodenajat = ("kevät", "kesä", "syksy", "talvi")
numero = int(input('Anna kuukauden numero (1-12)'))

if numero == 1 or numero == 2  or numero == 12:
    vuodenaika = vuodenajat[3]
elif numero == 3 or numero == 4 or numero == 5:
    vuodenaika = vuodenajat[0]
elif numero == 6 or numero == 7 or numero == 8:
    vuodenaika = vuodenajat[1]
elif numero == 9 or numero == 10 or numero == 11:
    vuodenaika = vuodenajat[2]



print (f"Kuukausi nro {numero} kuuluu {vuodenaika} vuodenaikaan.")

