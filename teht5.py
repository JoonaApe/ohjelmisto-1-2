import math

leiviska = int(input('Anna leiviskät '))
naulat = int(input('Anna naulat '))
luodit = float(input('Anna luodit '))

luotiPaino = 13.3
naulaPaino = 32 * luotiPaino
leiviskaPaino = 20 * naulaPaino

painoGram = (leiviskaPaino*leiviska) + (naulaPaino*naulat) + (luotiPaino*luodit)
painoKilo = painoGram/1000

print('Massa nykymittojen mukaan: ' +str(math.floor(painoKilo))+ ' kilogrammaa')