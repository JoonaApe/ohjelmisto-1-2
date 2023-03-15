pituus = int(input('Anna kuhan pituus senttimetreinä '))

pituus2 = 37-pituus

if pituus < 37:
    print('Kuha on alimittainen, laske se takaisin veteen. ' 'Kuhan tulisi olla '+str(pituus2)+ 'cm pidempi jotta se ei olisi alimittainen.' )
else:
    print("Hyvän kokonen kuha!")