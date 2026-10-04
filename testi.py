import random 

pelaajankolikot=random.randint(1,100)
monsterinkolikot=random.randint(1,100)


class Hahmo():
    def __init__(self, nimi, pelaajan_kolikot):
        self.nimi = nimi
        self.pelaajan_kolikot = pelaajan_kolikot 
        self.monsterin_kolikot = pelaajan_kolikot

    def tulosta_tiedot(self):
        print(f"hahmon nimi: {self.nimi}")
        print(f"hahmon kolikkomäärä: {self.pelaajan_kolikot}")

    def taistelu(self, vastus):
        print("ensimmäisen alueen taistelu!")
        print(f"{self.nimi} vastaan {vastus.nimi}")
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")

class Pelaaja(Hahmo):
    def __init__(self, nimi, kolikot):
        super().__init__(nimi,kolikot)




pelaaja1 = Pelaaja(input("anna pelaajalle nimi: "), pelaajankolikot)

pelaaja1.tulosta_tiedot()

avaruus_hirvio1 = Pelaaja("avaruus monsteri", monsterinkolikot)

avaruus_hirvio1.tulosta_tiedot()

pelaaja1.taistelu(avaruus_hirvio1)

