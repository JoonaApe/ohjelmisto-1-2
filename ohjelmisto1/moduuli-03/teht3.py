'''
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
'''
sukupuoli = input('Anna biologinen sukupuolesi. ')
hmgb = int(input('Anna hemoglobiinin arvosi '))

if sukupuoli  == 'nainen' and hmgb < 117:
    print('Hemoglobiini arvosi ovat liian matalat')
elif sukupuoli == 'nainen' and hmgb > 175:
    print('Hemoglobiini arvosi ovat liian korkeat')
elif sukupuoli == 'nainen' and hmgb >= 117 and hmgb <= 175:
    print('Hemoglobiini arvosi ovat normaalit')

elif sukupuoli == 'mies' and hmgb < 134:
    print('Hemoglobiini arvosi ovat liian matalat')
elif sukupuoli == 'mies' and hmgb > 195:
    print('Hemoglobiini arvosi ovat liian korkealla')
elif sukupuoli == 'mies' and hmgb >= 134 and hmgb<= 195:
    print('Hemoglobiini arvosi ovat normaalit.')