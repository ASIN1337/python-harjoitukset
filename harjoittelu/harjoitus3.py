class Esine:
    esineiden_maara = 0 
    def __init__(self, nimi, kuvaus, hinta):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.hinta = hinta
        Esine.esineiden_maara += 1

esine1 = Esine("vaasi", "hieno", 6.7)
esine2 = Esine("asin", "hienoin", 13.37)
print(esine1.nimi, esine1.kuvaus, esine1.hinta, Esine.esineiden_maara)
print(esine2.nimi, esine2.kuvaus, esine2.hinta, Esine.esineiden_maara)