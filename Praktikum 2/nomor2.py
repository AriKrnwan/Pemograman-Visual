# Nama : Ari kurniawan
# NIM  : 20051397057
# Kelas : D4 MI 2020A

class Tabung :

    def __init__(self, radius, tinggi):
        self.radius = radius
        self.tinggi = tinggi
        print('='*30)
        print('radius dari permukaan tabung tersebut adalah ', self.radius)
        print('tinggi dari tabung tersebut adalah ', self.tinggi)
        c = 22 / 7
        volume = c * self.radius ** 2 * self.tinggi
        print('-'*30)
        print('volume tabung tersebut adalah ', volume)
        print('='*30)

tabung = Tabung(7, 10)

class Balok:

    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.tinggi = tinggi
        self.lebar = lebar
        print('panjang dari balok tersebut adalah ', self.panjang)
        print('lebar dari balok tersebut adalah ', self.lebar)
        print('tinggi dari balok tersebut adalah ', self.tinggi)
        volume = self.panjang * self.lebar * self.tinggi
        print('-'*30)
        print('volume balok tersebut adalah ', volume)
        print('='*30)

balok = Balok(2, 3, 4)

class PrismaSegitiga:

    def __init__(self, alas, tinggi_s, tinggi_p):
        self.alas = alas
        self.tinggi_s = tinggi_s
        self.tinggi_p = tinggi_p
        print('panjang alas dari prisma segitiga tersebut adalah ', self.alas)
        print('tinggi alas dari prisma segitiga tersebut adalah ', self.tinggi_s)
        print('tinggi  dari prisma segitiga tersebut adalah ', self.tinggi_p)
        volume = (self.alas * self.tinggi_s / 2) * self.tinggi_p
        print('-'*30)
        print('volume prisma segitiga tersebut adalah ', volume)
        print('='*30)

prisma = PrismaSegitiga(3, 4, 10)