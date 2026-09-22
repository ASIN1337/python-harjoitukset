class Lentokone:
    def __init__(self, nimi, bensamaksimi, bensanykyinen):
        self.nimi=nimi
        self.maksimi_bensa=bensamaksimi
        self.nykyinen_bensa=bensanykyinen

    def Tankkaa():
        print(f"bensaa mahtui: {self.nimi.maksimi_bensa - self.nimi.nykyinen_bensa}")

    def Tulosta_tiedot():
        print()

class Lentokentta:
    def __init__(self):
        self.lentokoneet = []


    def Lentokone_sisaan(self, lentokone):
        self.lentokoneet.append(lentokone)
        print(f"kone {lentokone.nimi} tuli kentälle")
        return
        

    def Lentokone_ulos(self, lentokone):
        self.lentokoneet.remove(lentokone)
        print(f"kone {lentokone.nimi} lähti kentältä")
        return

    def Tulosta_koneet(self):
        print(self.lentokoneet)


lentokone1 = Lentokone("op", 400, 350)

vantaa = Lentokentta()

vantaa.Lentokone_sisaan(lentokone1)

Tulosta_tiedot(lentokone1)

                  
