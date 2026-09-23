class Pelaaja:
    def __init__(self, nimi, taso, pelaaja_ID):
        self.nimi = nimi
        self.taso = taso
        self.pelaaja_ID = pelaaja_ID
        self.esineet = []

    def level_up(self):
        self.taso += 1
    def lisaa_esine(self, esine):
            self.esineet.append(esine)

pelaaja4 = Pelaaja("sam", 1, 112233)
pelaaja4.lisaa_esine("miekka")
print(pelaaja4.esineet)