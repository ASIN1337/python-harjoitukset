class Opiskelija:
    def __init__(self, nimi, opiskelijanumero):
        self.nimi = nimi
        self.opiskelijanumero = opiskelijanumero
        self.kursseja = []

    def lisaa_kurssi(self, kurssi):
        self.kursseja.append(kurssi)

class Kurssi:
    def __init__(self, nimi, opintopisteet):
        self.nimi = nimi
        self.opintopisteet = opintopisteet
        self.opiskelijat = []

    def lisaa_opiskelija(self, opiskelija):
        self.opiskelijat.append(opiskelija)

#Pääohjelma
#Luo joitain Opiskelija- ja kurssiolioita, ja kokeile luokkiesi toimivuutta

opiskelija1 = Opiskelija("asin", 1337)
kurssi1 = Kurssi("ohjelmointi 1", 500)

kurssi1.lisaa_opiskelija(opiskelija1)
print(kurssi1.opiskelijat)

opiskelija1.lisaa_kurssi(kurssi1)
print(opiskelija1.kursseja)