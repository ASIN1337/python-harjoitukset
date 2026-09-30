class Hahmo:
    def __init__(self, nimi, hp):
        self.nimi = nimi
        self.hp = hp

    def tulosta_tiedot(self):
        print(f'Hahmon nimi: {self.nimi}')
        print("Hahmon hp:", self.hp)

    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        input()
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            self.tulosta_tiedot()