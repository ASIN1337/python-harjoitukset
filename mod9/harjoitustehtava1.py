class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus =rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        if self.tamanhetkinen_nopeus + muutos <= 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus + muutos >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        else:
            self.tamanhetkinen_nopeus += muutos


    def kulje(self, aika):
        self.kuljettu_matka = self.tamanhetkinen_nopeus * aika

         

auto1 = Auto("ABC-123",142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"auton nopeus nyt:  {auto1.tamanhetkinen_nopeus}")
auto1.kiihdyta(-10)
print(f"auton nopeus nyt: {auto1.tamanhetkinen_nopeus}")

auto1.kulje(3)
print(f"kuljettu matka on {auto1.kuljettu_matka} ja auton nopeus on {auto1.tamanhetkinen_nopeus}")

print(f"rekisteritunnus {auto1.rekisteritunnus} nopeus {auto1.huippunopeus} tämänhetkinen nopeus {auto1.tamanhetkinen_nopeus} kuljettu matka {auto1.kuljettu_matka}")