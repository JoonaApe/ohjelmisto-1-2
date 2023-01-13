import math

leiviska = int(input('Anna leiviskät '))
naulat = int(input('Anna naulat '))
luodit = float(input('Anna luodit '))

luotiPaino = 13.3
naulaPaino = 32 * luotiPaino
leiviskaPaino = 20 * naulaPaino

kokonaisPaino = (leiviskaPaino*leiviska) + (naulaPaino*naulat) + (luotiPaino*luodit)
painoKilo = kokonaisPaino/1000
painoGram = kokonaisPaino - (math.floor(painoKilo)*1000)
painoGram2 = "%.2f" % painoGram



print('Massa nykymittojen mukaan: ' +str(math.floor(painoKilo))+ ' kilogrammaa ja ' +str(painoGram2)+ ' grammaa')