import random 

pelaajankolikot = random.randint(1,500)
monsterinkolikot = random.randint(1,100)

class Paavalikko():
    def __init__(self, pelaajan_kolikot):
        self.pelaajan_kolikot = pelaajan_kolikot
        kayttajan_nimi = input("Anna käyttäjän nimi: ")
        selvitys = int(input("Anna ikäsi: "))
        print(f"käyttäjän nimi: {kayttajan_nimi}")
        print(f"käyttäjän ikä: {selvitys}")

         
        if selvitys < 12:
            print("käyttäjä on alaikäinen")
            print("peli suljetaan")
        

        if selvitys >= 12:
            print(f"Hei! {kayttajan_nimi} Tervettuloa peliin!")
            while True:
                print("päävalikko!!")
                komento = input("Anna komento ""a""/aloita peli ""r""/uhkapelaus: ")

                if komento == "r":
                    self.pelaa_random(pelaajankolikot)

                if komento == "a":
                    break

    def pelaa_random(self, pelaajan_kolikot):                
        self.pelaajan_kolikot = pelaajan_kolikot
        while True:
            random_komento = input("haluatko pelata random konetta k/kyllä vai e/ei: ")
            random1 = random.randint(1,2)
            if random_komento == "k":
                if random1 == 1:
                    print(f"OLET SAANUT ONGEN!! ESINEEN ARVO ON 5 KOLIKKOA!!")
                    tulos = self.pelaajan_kolikot + 5
                    return tulos
                            
                if random1 == 2:
                    print("OLET SAANUT AUTON!! ESINEEN ARVO ON 50 KOLIKKOA")
                    tulos = self.pelaajan_kolikot + 50
                    return tulos
                            
            if random_komento == "e":
                break

    
    
class Hahmo(Paavalikko):
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

        

Paavalikko(pelaajankolikot)

pelaaja1 = Pelaaja(input("anna pelaajalle nimi: "), pelaajankolikot)

pelaaja1.tulosta_tiedot()

avaruus_hirvio1 = Pelaaja("avaruus monsteri", monsterinkolikot)

avaruus_hirvio1.tulosta_tiedot()

pelaaja1.taistelu(avaruus_hirvio1)