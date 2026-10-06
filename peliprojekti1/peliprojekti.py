import random 
import sys      #tämän käyttö siihen että peli suljetaan jos pelaaja on alaikäinen 

pelaajankolikot = random.randint(1,250)
monsterinkolikot = random.randint(1,100)
tallinnamonsterikolikot = random.randint(1,175)
hmlmonsterikolikot = random.randint(1,50)

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
            random1 = random.randint(1,16)

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

                if random1 == 6:
                    print("OLET SAANUT ESINEEN NUKKE NIMELTÄ RESSU!!!!! ESINEEN ARVO ON 1000 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 1000
                    return pelaajankolikot

                if random1 == 7:
                    print("OLET SAANUT ESINEEN KIRVES!! ESINEEN ARVO ON 4 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 4
                    return pelaajankolikot

                if random1 == 8:
                    print("OLET SAANUT PAAVO PESUSIENI SUKAT!! ESINEEN ARVO ON 10 KOLIKKOA")
                    print("vasemmassa sukassa on reikä...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 10
                    return pelaajankolikot

                if random1 == 9:
                    print("OLET SAANUT ESINEEN PYJAMA HOUSUT!! ESINEEN ARVO ON 5 KOLIKKOA")
                    print("housuissa on jostakin syystä monta reikää...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot

                if random1 == 10:
                    print("OLET SAANUT ESINEEN LÄPPÄRI!!!! ESINEEN ARVO ON 50 KOLIKKOA")
                    print("läppärin kannessa on monta tarraa...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 50
                    return pelaajankolikot

                if random1 == 11:
                    print("OLET SAANUT ESINEEN BANAANIPIRTELÖ!! ESINEEN ARVO ON 15 KOLIKKOA")
                    print("ainekset 2 banaania, 0.5 L vaniljajäätelöä, 2 DL maitoa ja vähän vaniljasokeria")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 15
                    return pelaajankolikot

                if random1 == 12:
                    print("OLET SAANUT ESINEEN SESSUN HIKISET SUKAT..!! ESINEEN ARVO ON 67 KOLIKKOA")
                    print("...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 67
                    return pelaajankolikot

                if random1 == 13:
                    print("OLET SAANUT ESINEEN PUHELIN!! ESINEEN ARVO ON 100 KOLIKKOA")
                    print("puhelimessta roikkuu puhelin koru...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 100
                    return pelaajankolikot

                if random1 == 14:
                    print("OLET SAANUT ESINEEN MIKUN PAITA!! ESINEEN ARVO ON 67 KOLIKKOA")
                    print("tuoksuu hyvältä")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 67
                    return pelaajankolikot

                if random1 == 15:
                    print("OLET SAANUT ESINEEN liandryn piina...?? esineen arvo on 0 kolikkoa...?")
                    print("kyseinen reliikki on hyödytön kuolevaisille, mutta oikessa käsissä voittamaton")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 0
                    return pelaajankolikot
                
                if random1 == 16:
                    print("OLET SAANUT ESINEEN KISSA PEHMOLELU!! ESINEEN ARVO ON 22 KOLIKKOA")
                    print("pörröinen, pieni ja pehmeä")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    pelaajankolikot = self.pelaajan_kolikot + 22
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
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")

    def taistelu_tallinna(self, vastus):
        print("areena Tallinna taistelu!")
        print(f"{self.nimi} vastaan {vastus.nimi}")
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")

    def taistelu_hml(self, vastus):
        print("areena HÄMEENLINNA taistelu!!!!")
        print(f"{self.nimi} vastaan {vastus.nimi}")
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")


class Pelaaja(Hahmo):
    def __init__(self, nimi, kolikot, uusi_areena, nykyinen_areena):
        self.uusi_areena = uusi_areena
        self.nykyinen_areena = nykyinen_areena
        super().__init__(nimi,kolikot)



    def siirry_areenalle_eka(self, minne):
        self.minne = minne
        if minne == "1":
            print("sinut siirretään areenalle Avaruus.")
            self.nykyinen_areena == "avaruus"
            self.eka_areena()

        if minne == "2":
            print("sinut siirretään areenalle Tallinna.")
            #toka_areena()

        if minne == "3":
            print("sinut siirretään areenalle Hämeenlinnan pizza melodi")
            #kolmas_areena()

    def siirry_areenalle1(self, minne, nykyinen_areena):
        self.nykyinen_areena = nykyinen_areena
        if minne == 2 or minne == 3 and minne != 1:
            if minne == 2:
                self.toka_areena()

            if minne == 3:
                self.kolmas_areena()

    def siirry_areenalle2(self, minne, nykyinen_areena):
        self.nykyinen_areena = nykyinen_areena
        if minne == 3 and minne != 1 or 2:
            if minne == 3:
                self.kolmas_areena()

    def eka_areena(self):
        pelaaja1.tulosta_tiedot()
        avaruus_hirvio1.tulosta_tiedot()
        pelaaja1.taistelu(avaruus_hirvio1)
        self.minne = 2
        seuraava_areena = input("valitse seuraava areena ""2""/Tallinna ""3""/Hämeenlinnan pizza melodi: ")
        if seuraava_areena == "2":
            self.siirry_areenalle1(2,1)
        
    def toka_areena(self):
        pelaaja1.tulosta_tiedot()
        tallinnan_monsteri.tulosta_tiedot()
        pelaaja1.taistelu_tallinna(tallinnan_monsteri)
        kolmas_areena = input("valitse seuraava areena ""3""/hämeenlinnan pizza melodi: ")
        if kolmas_areena == "3":
            self.siirry_areenalle2(3,2)
        
    def kolmas_areena(self):
        pelaaja1.tulosta_tiedot()
        hml_monsteri.tulosta_tiedot()
        pelaaja1.taistelu_hml(hml_monsteri)       
        print("ONNITTELUT VOITIT PELIN!!!! ")
        sys.exit() 

Paavalikko(pelaajankolikot)

print("peli aloitetaan!")

avaruus_hirvio1 = Pelaaja("avaruus monsteri", monsterinkolikot, 1, 0)

tallinnan_monsteri = Pelaaja("mik", tallinnamonsterikolikot, 2, 2)

hml_monsteri = Pelaaja("mare", hmlmonsterikolikot, 3, 3)

pelaajan_nimi=input("anna pelaajallesi nimi: ")

valitse_areena = input("Valitse areena mihin haluat mennä ""1""/avaruus ""2""/tallinna ""3""/hämeenlinnan pizza melodi: ")

pelaaja1 = Pelaaja(pelaajan_nimi, pelaajankolikot, valitse_areena, 0)

pelaaja1.siirry_areenalle_eka(valitse_areena)

#pelaaja1.tulosta_tiedot()

#avaruus_hirvio1.tulosta_tiedot()

#pelaaja1.taistelu(avaruus_hirvio1)
