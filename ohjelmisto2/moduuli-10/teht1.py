'''
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
Jos teet luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_
ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.
'''

class Hissi:
    def __init__(self, alin_kerros = 1, ylin_kerros = 10):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")

    def siirry_kerrokseen(self, uusi_kerros):
        while self.kerros != uusi_kerros:
            if self.kerros < uusi_kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()



h = Hissi()

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin_kerros)

