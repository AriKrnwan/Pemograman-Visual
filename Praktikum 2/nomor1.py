# Nama : Ari kurniawan
# NIM  : 20051397057
# Kelas : D4 MI 2020A

class Persegi:

    def __init__(self, sisi):
        self.sisi = sisi
        print('='*30)
        print('sisi dari persegi adalah ', self.sisi)
        luas = self.sisi * 2
        keliling = self.sisi * 4
        print('-'*30)
        print('luas persegi adalah ', luas)
        print('keliling persegi adalah ', keliling)
        print('='*30)
        
persegi = Persegi(5)


class Segitiga:

    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        print('alas dari segitiga adalah ', self.alas)
        print('tinggi dari segitiga adalah ', self.tinggi)
        luas = (self.alas * self.tinggi) / 2
        miring = (self.alas ** 2 + self.tinggi ** 2) ** 0.5
        keliling = self.alas + self.tinggi + miring
        print('-'*30)
        print('luas segitiga adalah ', luas)
        print('keliling segitiga adalah ', keliling)
        print('='*30)

segitiga = Segitiga(3, 4)

class Jajargenjang:

    def __init__(self, alas, tinggi, miring):
        self.alas = alas
        self.tinggi = tinggi
        self.miring = miring
        print('alas dari jajar genjang adalah ', self.alas)
        print('tinggi dari jajar genjang adalah ', self.tinggi)
        print('sisi miring dari jajar genjang adalah ', self.miring)
        luas = self.alas * self.tinggi
        keliling = 2 * self.alas + 2 * self.miring
        print('-'*30)
        print('luas jajar genjang adalah ', luas)
        print('keliling jajar genjang adalah ', keliling)
        print('='*30)

jajargenjang = Jajargenjang(3, 4, 5)

