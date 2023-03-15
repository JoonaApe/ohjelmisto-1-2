'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
'''
nums = []

while True:
    num = input('Anna numeroita tai lopeta painamalla Enter. ')

    if not num:
        break
    num = int(num)
    nums.append(num)

nums.sort(reverse=True)
for i in range(5):
    print(nums[i])