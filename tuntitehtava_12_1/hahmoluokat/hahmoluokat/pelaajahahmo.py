class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, hp, tavaralista):
        super().__init__(nimi, hp)
        self.tavarat = tavaralista

    def tulosta_tavarat(self):
        print("Hahmolla on:")
        for t in self.tavarat:
            print(t)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        self.tulosta_tavarat()
        print("\n")