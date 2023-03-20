'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

'''

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, hissi_nro = 0):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_nro = hissi_nro
    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi {self.hissi_nro} on nyt kerroksessa {self.kerros}.")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi {self.hissi_nro} on nyt kerroksessa {self.kerros}.")

    def siirry_kerrokseen(self, uusi_kerros):
        while self.kerros != uusi_kerros:
            if self.kerros < uusi_kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lkm):
        self.alin_kerros = alin_kerros
        self.hissit = []
        for i in range(hissi_lkm):
            self.hissit.append(Hissi(alin_kerros,ylin_kerros,i+1))

    def aja_hissi(self,hissi_nro, uusi_kerros):
        hissi = self.hissit[hissi_nro -1]
        print(f"Hissi numero {hissi_nro} liikkuu nyt.")
        hissi.siirry_kerrokseen(uusi_kerros)
        print(f"Hissi numero {hissi_nro} on pysähtynyt.")

    def palohalytys(self):
        print("\nPALOHÄLYTYS! Kaikki hissit menevät alimpaan kerrokseen.")
        for hissi in self.hissit:
            if hissi.kerros > 1:
                print(f"\nHissi numero {hissi.hissi_nro} liikkuu nyt.")
                hissi.siirry_kerrokseen(self.alin_kerros)
            else:
                print(f"\nHissi {hissi.hissi_nro} on jo alimmassa kerroksessa.\n")



talo = Talo(1,10,5)
talo.aja_hissi(2,3)
talo.aja_hissi(3,5)
talo.palohalytys()