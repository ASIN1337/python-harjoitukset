class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.AlinKerros = alin_kerros
        self.YlinKerros = ylin_kerros
        self.NykyinenKerros = alin_kerros

    def siirry_kerrokseen(self, minne):
        while self.NykyinenKerros != minne:
            if self.NykyinenKerros < minne:
                self.kerros_ylös()
                
            elif self.NykyinenKerros >= minne:
                self.kerros_alas()
        print("olet perillä!")
               
    def kerros_ylös(self):
        self.NykyinenKerros += 1
        if self.NykyinenKerros > self.YlinKerros:
            self.NykyinenKerros = self.YlinKerros
        print(f"olet kerroksessa {self.NykyinenKerros}")
        
    def kerros_alas(self):
        self.NykyinenKerros -= 1
        if self.NykyinenKerros < self.AlinKerros:
            self.NykyinenKerros = self.AlinKerros
        print(f"olet kerroksessa {self.NykyinenKerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros):
        self.AlinKerros = alin_kerros
        self.YlinKerros = ylin_kerros
        self.hissit = []

    def lisaa_hissi(self, hissi):
        self.hissit.append(hissi)
        
    def aja_hissia(self, hissi, kohde):
        hissi.siirry_kerrokseen(kohde)
        
#h = Hissi(1, 7)

#h.siirry_kerrokseen(5)

#h.siirry_kerrokseen(h.AlinKerros)

ylin = int(input("anna talon ylin kerros: "))
alin = int(input("anna talon alin kerros: "))
talo = Talo(alin, ylin)
hissit = int(input("montako hissia talossa on: "))
for hissi in range(hissit):
    hissi = Hissi(alin, ylin)
    talo.lisaa_hissi(hissi)

nappi = "0"
while nappi != "2":
    nappi = input("1. käytä hissiä 2. lopeta ")
    if nappi == "1":
        hissi = int(input("mikä hissin numero: "))
        hissi -= 1
        kohde = int(input("mihin kerrokseen: "))
        talo.aja_hissia(talo.hissit[hissi], kohde)

