# contoh class

class Orang:
    pass
org = Orang()
print (org)

# contoh method obyek

class Orang:
    def katakanHaiGANTENX(self):
        print('HaiGANTENX, pakabar ?')
org = Orang()
org.katakanHaiGANTENX()

# contoh method init

class Orang:
    def __init__(self, nama):
        self.nama = nama
    def katakanHaiGANTENX(self):
        print ('Halo, nama saya %s, apa kabar ?' % self.nama)
org = Orang('mas')
org.katakanHaiGANTENX()