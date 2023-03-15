'''
pii tehtävä
'''
import random

N = int(input('Anna arvottavien pisteiden määrä '))
counter = 0
n = 0
while counter < N:
    counter += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'arvottu piste {x}, {y}')

    if x**2 + y**2 < 1:
        print('On sisällä')
        n += 1
print(f'Pisteitä arvottu yhteensä {counter}, joista {n} kpl ympyrän sisällä')

if N == counter:
    pii = 4*n/N
    print(f'Piin likiarvo annetuilla pisteillä {pii}')

