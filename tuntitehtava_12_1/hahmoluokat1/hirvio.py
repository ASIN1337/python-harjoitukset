from .hahmo import Hahmo
class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki, hp):
        super().__init__(nimi, hp)
        self.repliikki = repliikki

    def tulosta_tiedot(self):
        print(self.repliikki)
        super().tulosta_tiedot()
        print("\n")