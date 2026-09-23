class Kentta:
    def __init__(self, kentta_ID, nimi, kuvaus):
        self.kentta_ID = kentta_ID
        self.nimi = nimi
        self.kuvaus = kuvaus

olio1 = Kentta(1337, "asin", "ei niin lihaksikas")
olio2 = Kentta(67, "emppu", "melko lihaksikas")

print(olio1.nimi, olio1.kuvaus)
print(olio2.nimi, olio2.kuvaus)