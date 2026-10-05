import random 
import sys      #tämän käyttö siihen että peli suljetaan jos pelaaja on alaikäinen 

pelaajankolikot = random.randint(1,250)
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
            sys.exit()

        if selvitys >= 12:
            print(f"Hei! {kayttajan_nimi} Tervettuloa peliin!")
            while True:
                print("päävalikko!!")
                komento = input("Anna komento ""a""/aloita peli ""r""/uhkapelaus ""c""/kolikoiden tarkastus: ")

                if komento == "c":
                    print(f"pelaajan tämänhetkinen kolikkomäärä on {pelaajankolikot}")

                if komento == "r":
                    self.pelaa_random(pelaajankolikot)

                if komento == "a":
                    break

    def pelaa_random(self, pelaajan_kolikot):                
        self.pelaajan_kolikot = pelaajan_kolikot
        global pelaajankolikot          #Netistä löydetty "global jolla saan funktiosta arvon palautettua pääohjelmaan lisätietoa readme tiedostossa"
        while True:                     
            random_komento = input("haluatko pelata random konetta k/kyllä vai e/ei: ")
            random1 = random.randint(1,5)

            if random_komento == "k":
                if random1 == 1:
                    print(f"OLET SAANUT ONGEN!! ESINEEN ARVO ON 5 KOLIKKOA!!")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot
                            
                if random1 == 2:
                    print("OLET SAANUT AUTON!! ESINEEN ARVO ON 50 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 50
                    return pelaajankolikot

                if random1 == 3:
                    print("OLET SAANUT ESINEEN OMITUINEN HATTU!! ESINEEN ARVO ON 10 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 10
                    return pelaajankolikot

                if random1 == 4:
                    print("OLET SAANUT ESINEEN KÄYTETTY BOXERI!! ESINEEN ARVO ON 0 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 0
                    return pelaajankolikot

                if random1 == 5:
                    print("OLET SAANUT ESINEEN OMENA!!!!!! ESINEEN ARVO ON 500 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 500
                    return pelaajankolikot

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
