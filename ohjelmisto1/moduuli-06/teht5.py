'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi
että siitä on karsittu pois kaikki parittomat luvut.

Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
'''

def parilliset_luvut(lista_parametri):
    muokattu_lista = []
    for i in lista_parametri:
        if i % 2 == 0:
            muokattu_lista.append(i)
    return muokattu_lista



numerot = [1,213,4,21,51,12,5,520,8,6]
print(f'alkuperäinen lista: {numerot}')
print(f'karsittu lista: {parilliset_luvut(numerot)}')

