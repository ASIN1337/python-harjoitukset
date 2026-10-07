import random 
import sys      #tämän käyttö siihen että peli suljetaan jos pelaaja on alaikäinen 

def tulosta_intro():
    with open("peliprojekti1/ohje/intro.txt", "r", encoding="utf-8") as tiedosto:
        intro = tiedosto.read()
        print(intro)

def tulosta_ohjeet():
    with open("peliprojekti1/ohje/ohjeet.txt", "r", encoding="utf-8") as tiedosto:
        ohje = tiedosto.read()
        print(ohje)

pelaajankolikot = random.randint(1,50)
monsterinkolikot = random.randint(1,100)

marsmonsterinkolikot = random.randint(1,20)
jupitermonsterinkolikot = random.randint(1,50)      #Alue avaruus monsteriden kolikko generointi
kuumonsterinkolikot = random.randint(45,100)

tallinnamonsterikolikot = random.randint(50,175)
satamamonsterinkolikot = random.randint(1,20)           #Alue viro monstereiden kolikko generointi
vanhakaupunkimonsterinkolikot = random.randint(100, 500)

hmlmonsterikolikot = random.randint(1,15)
katumamonsterikolikot = random.randint(1,25)            #Alue Hämeenlinna monstereiden kolikko generointi
visamakimonsterikolikot = random.randint(200,450)
jukolamonsterikolikot = random.randint(50,250)

kidemonsterinkolikot = random.randint(50,150)
krismonsterinkolikot = random.randint(50,150)           #lohjan monstereiden kolikko generointi
prismamonsterinkolikot = kidemonsterinkolikot + krismonsterinkolikot

class Paavalikko():                                 #päävalikko ja sen sisällä loop
    def __init__(self, pelaajan_kolikot):
        self.pelaaja_kolikot = pelaajan_kolikot
        kayttajan_nimi = input("Anna käyttäjän nimi: ")
        selvitys = int(input("Anna ikäsi: "))
        print("..........................................................................................") #tämä vain ulkonäön takia varmaan olisi ollut nätimpiä keinoja mutta omaa käsialaa ainakin
        print(f"käyttäjän nimi: {kayttajan_nimi}")
        print(f"käyttäjän ikä: {selvitys}")
        print("..........................................................................................")
         
        if selvitys < 12:
            print("käyttäjä on alaikäinen")
            print("peli suljetaan")
            sys.exit()      #peli suljetaan/lakkaa toimimasta

        if selvitys >= 12:
            print(f"Hei! {kayttajan_nimi} Tervettuloa peliin!")
            print("..........................................................................................")
            while True:
                print("päävalikko!!")
                komento = input("Anna komento ""a""/aloita peli o/ohjeet i/intro ""r""/uhkapelaus ""c""/kolikoiden tarkastus: ")

                if komento == "c":
                    lapi = range(6)     #tämä ulkonäön takia kanssa. luo 6 riviä tyhjää printtiä. netistä löydetty.
                    for n in lapi:
                        print()
                    print("..........................................................................................")
                    print()
                    print(f"pelaajan tämänhetkinen kolikkomäärä on {pelaajankolikot}")
                    print()
                    print("..........................................................................................")

                if komento == "r":
                    self.pelaa_random(pelaajankolikot)

                if komento == "o":
                    tulosta_ohjeet()

                if komento == "i":
                    tulosta_intro()

                if komento == "a" and pelaajankolikot == 222:
                    print("ONNITTELUT LÖYSIT SALAISEN VOITON !!!!!")
                    sys.exit()

                if komento == "a":
                    break

    def pelaa_random(self, pelaajan_kolikot):               #random masiinan toiminta
        self.pelaajan_kolikot = pelaajan_kolikot
        global pelaajankolikot          #Netistä löydetty "global jolla saan funktiosta arvon palautettua pääohjelmaan lisätietoa readme tiedostossa"
        while True:
            print("..........................................................................................")
            lapi = range(6)
            for n in lapi:
                print()
            print("..........................................................................................")
            random_komento = input("haluatko pelata random konetta k/kyllä vai e/ei: ")      #esine kolikko masiinan (uhkapelaus)
            print("..........................................................................................")
            lapi = range(6)
            for n in lapi:
                print()

            random1 = random.randint(1,60)

            if random_komento == "k":
                if random1 == 1:
                    print("..........................................................................................")
                    print(f"OLET SAANUT ONGEN!! ESINEEN ARVO ON 5 KOLIKKOA!!")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot
                            
                if random1 == 2:
                    print("..........................................................................................")
                    print("OLET SAANUT AUTON!! ESINEEN ARVO ON 50 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 50
                    return pelaajankolikot

                if random1 == 3:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN OMITUINEN HATTU!! ESINEEN ARVO ON 10 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 10
                    return pelaajankolikot

                if random1 == 4:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KÄYTETTY BOXERI!! ESINEEN ARVO ON 0 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 0
                    return pelaajankolikot

                if random1 == 5:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN OMENA!!!!!! ESINEEN ARVO ON 500 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 500
                    return pelaajankolikot

                if random1 == 6:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN NUKKE NIMELTÄ RESSU!!!!! ESINEEN ARVO ON 1000 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1000
                    return pelaajankolikot

                if random1 == 7:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KIRVES!! ESINEEN ARVO ON 4 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 4
                    return pelaajankolikot

                if random1 == 8:
                    print("..........................................................................................")
                    print("OLET SAANUT PAAVO PESUSIENI SUKAT!! ESINEEN ARVO ON 10 KOLIKKOA")
                    print("vasemmassa sukassa on reikä...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 10
                    return pelaajankolikot

                if random1 == 9:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PYJAMA HOUSUT!! ESINEEN ARVO ON 5 KOLIKKOA")
                    print("housuissa on jostakin syystä monta reikää...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot

                if random1 == 10:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN LÄPPÄRI!!!! ESINEEN ARVO ON 50 KOLIKKOA")
                    print("läppärin kannessa on monta tarraa...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 50
                    return pelaajankolikot

                if random1 == 11:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN BANAANIPIRTELÖ!! ESINEEN ARVO ON 15 KOLIKKOA")
                    print("ainekset 2 banaania, 0.5 L vaniljajäätelöä, 2 DL maitoa ja vähän vaniljasokeria")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 15
                    return pelaajankolikot

                if random1 == 12:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN SESSUN HIKISET SUKAT..!! ESINEEN ARVO ON 67 KOLIKKOA")
                    print("...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 67
                    return pelaajankolikot

                if random1 == 13:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PUHELIN!! ESINEEN ARVO ON 100 KOLIKKOA")
                    print("puhelimessta roikkuu puhelin koru...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 100
                    return pelaajankolikot

                if random1 == 14:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN MIKUN PAITA!! ESINEEN ARVO ON 67 KOLIKKOA")
                    print("tuoksuu hyvältä")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 67
                    return pelaajankolikot

                if random1 == 15:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN liandryn piina...?? esineen arvo on 0 kolikkoa...?")
                    print("kyseinen reliikki on hyödytön kuolevaisille, mutta oikessa käsissä voittamaton")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 0
                    return pelaajankolikot
                
                if random1 == 16:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KISSA PEHMOLELU!! ESINEEN ARVO ON 22 KOLIKKOA")
                    print("pörröinen, pieni ja pehmeä")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 22
                    return pelaajankolikot

                if random1 == 17:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN SPOTIFY PREMIUM KUPONKI!! ESINEEN ARVO ON 43 KOLIKKOA")
                    print("voimassa 2 vuotta")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 43
                    return pelaajankolikot

                if random1 == 18: 
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KAHVIKUPPI! ESINEEN ARVO ON 3 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 3
                    return pelaajankolikot

                if random1 == 19:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN DND NOPPA!! ESINEEN ARVO ON 5 KOLIKKOA")
                    print("siinä on 20 puolta!")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot

                if random1 == 20:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KYNSI! ESINEEN ARVO ON 1 KOLIKKO")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1
                    return pelaajankolikot

                if random1 == 21:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN  MUSTA TAKKI! ESINEEN ARVO ON 20 KOLIKKOA")
                    print("onpas lämmin")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 20
                    return pelaajankolikot

                if random1 == 22:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KUULOKKEET! ESINEEN ARVO ON 200 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 200
                    return pelaajankolikot

                if random1 == 23:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN LATURI! ESINEEN ARVO ON 2 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 2
                    return pelaajankolikot

                if random1 == 24:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN TUOLI! ESINEEN ARVO ON 5 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot

                if random1 == 25:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PUNAINEN TUOLI! ESINEEN ARVO ON 6 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 6
                    return pelaajankolikot

                if random1 == 26:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN MUSTA TIETOKONE! ESINEEN ARVO ON 10 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 10
                    return pelaajankolikot

                if random1 == 27:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN REPPU! ESINEEN ARVO ON 2 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 2
                    return pelaajankolikot

                if random1 == 28:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN VYÖ! ESINEEN ARVO ON 2 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 2
                    return pelaajankolikot

                if random1 == 29:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PAPERI! ESINEEN ARVO ON 1 KOLIKKO")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1
                    return pelaajankolikot 
                if random1 == 30:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PÖYTÄ! ESINEEN ARVO ON 7 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 7
                    return pelaajankolikot

                if random1 == 31:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN MUKI! ESINEEN ARVO ON 5 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot

                if random1 == 32:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PIKACHU MUKI!!! ESINEEN ARVO ON 20 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 20
                    return pelaajankolikot

                if random1 == 33:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN VIHKO! ESINEEN ARVO ON 3 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 3
                    return pelaajankolikot 
                if random1 == 34:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KYNÄ! ESINEEN ARVO ON 2 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 2
                    return pelaajankolikot

                if random1 == 35:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KUMI! ESINEEN ARVO ON 2 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 2 
                    return pelaajankolikot

                if random1 == 36:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN TEROITIN! ESINEEN ARVO ON 1 KOLIKKO")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1
                    return pelaajankolikot

                if random1 == 37:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN VIIVOITIN! ESINEEN ARVO ON 1 KOLIKKO")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1
                    return pelaajankolikot

                if random1 == 38:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN TUSSI! ESINEEN ARVO ON 1 KOLIKKO")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1 
                    return pelaajankolikot

                if random1 == 39:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PURUKUMI PUSSI! ESINEEN ARVO ON 3 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 3
                    return pelaajankolikot

                if random1 == 40:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PENAALI! ESINEEN ARVO ON 4 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 4
                    return pelaajankolikot 

                if random1 == 41:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN LOMPAKKO! ESINEEN ARVO ON 0 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 0 
                    return pelaajankolikot

                if random1 == 42:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN LASKIN! ESINEEN ARVO ON 7 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 7
                    return pelaajankolikot
                if random1 == 43:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN VESIMELONI REDBULL!! ESINEEN ARVO ON 50 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 50
                    return pelaajankolikot

                if random1 == 44:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KAULAKORU!! ESINEEN ARVO ON 99 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 99
                    return pelaajankolikot

                if random1 == 45:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN HIIRI! ESINEEN ARVO ON 2 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 2
                    return pelaajankolikot

                if random1 == 46:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN NÄPPÄIMISTÖ! ESINEEN ARVO ON 1 KOLIKKO")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1
                    return pelaajankolikot

                if random1 == 47:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN HIIRIMATTO! ESINEEN ARVO ON 1 KOLIKKO")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 1
                    return pelaajankolikot

                if random1 == 48:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN AVAIN! ESINEEN ARVO ON 4 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 4
                    return pelaajankolikot

                if random1 == 49:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN AVAIMENPERÄ! ESINEEN ARVO ON 4 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 4
                    return pelaajankolikot

                if random1 == 50:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN TARRA! ESINEEN ARVO ON 4 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 4
                    return pelaajankolikot

                if random1 == 51:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN RANNEKE! ESINEEN ARVO ON 5 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot

                if random1 == 52:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN BATMAN PEHMOLELU!! ESINEEN ARVO ON 10 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 10
                    return pelaajankolikot

                if random1 == 53:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN KIDEN SUKKA!! ESINEEN ARVO 10 KOLIKKOA")
                    print("todella haiseva sukka...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 10
                    return pelaajankolikot

                if random1 == 54:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN JONNAN HAISEVA SUKKA! ESINEEN ARVO ON 5 KOLIKKOA")
                    print("todella todella haisevat...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 5
                    return pelaajankolikot

                if random1 == 55:
                    print("..........................................................................................")
                    print("OLET SAANUT KRISUN HAISEVAN SUKAN! ESINEEN ARVO ON 6 KOLIKKOA")
                    print("miten sukat voivat haista näin paljon...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 6
                    return pelaajankolikot

                if random1 == 56:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN MATKALAUKKU! ESINEEN ARVO ON 3 KOLIKKOA")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 3
                    return pelaajankolikot

                if random1 == 57:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN NUUDELI PAKETTI! ESINEEN ARVO ON 100 KOLIKKOA")
                    print("nammmm... rakkaat nuudelit...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 100
                    return pelaajankolikot                

                if random1 == 58:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN PEHMOLELU FANSKU!!! ESINEEN ARVO ON 500 KOLIKKOA")
                    print("fansku parhain koira ikinä...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot + 500
                    return pelaajankolikot

                if random1 == 59:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN LASKU! ESINEEN ARVO ON -700 KOLIKKOA")
                    print("KOLIKOT OTETAAN HAHMOLTASI")
                    print("..........................................................................................")
                    pelaajankolikot = self.pelaajan_kolikot - 700
                    return pelaajankolikot

                if random1 == 60:
                    print("..........................................................................................")
                    print("OLET SAANUT ESINEEN OMPUN SUKAT! ESINEEN ARVO ON 20 KOLIKKOA")
                    print("tuoksuupas hyvältä...")
                    print("KOLIKOT ANNETAAN HAHMOLLESI")
                    print("..........................................................................................")
                    pelaajankolikot =self.pelaajan_kolikot + 20
                    return pelaajankolikot
                
            if random_komento == "e":
                break

class Hahmo():      #tästä peritään hahmoille nimet ja kolikot sekä eri toimintoja
    def __init__(self, nimi, pelaajan_kolikot):
        self.nimi = nimi
        self.pelaajan_kolikot = pelaajan_kolikot 
        self.monsterin_kolikot = pelaajan_kolikot

    def tulosta_tiedot(self):       #yksiselitteinen
        print("..........................................................................................")
        print(f"hahmon nimi: {self.nimi}")
        print(f"hahmon kolikkomäärä: {self.pelaajan_kolikot}")
        print("..........................................................................................")

    def monsterin_tiedot(self):     #yksiselitteinen
        print("..........................................................................................")
        print(f"vastuksen nimi: {self.nimi}")
        print(f"vastuksen kolikkomäärä: {self.monsterin_kolikot}")
        print("..........................................................................................")

    def taistelu(self, vastus):         #tästä alkaa eri alueiden taistelut
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
        print("areena Pizzeria melodi taistelu!!!!")
        input()     #hyvä menetelmä pitää pelaaja edelleen toiminnassa ja jakaaa tekstiä erittäin hyvin
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()


    def taistelu_jukola(self, vastus):
        print("areena Jukola taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()


    def taistelu_katuma(self, vastus):
        print("areena Katuma taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

    def taistelu_visamaki(self, vastus):
        print("areena Visamäki taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

    def taistelu_satama(self, vastus):
        print("areena Tallinnan satama taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

    def taistelu_vanha(self, vastus):
        print("areena Tallinna vanha kaupunki taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

    def taistelu_mars(self, vastus):
        print("areena Mars taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

    def taistelu_jupiter(self, vastus):
        print("areena Jupiter taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

    def taistelu_kuu(self, vastus):
        print("areena Kuu taistelu!!!!")
        input()
        print(f"{self.nimi} vastaan {vastus.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä on : {self.pelaajan_kolikot} vastustajan kolikkomäärä on: {vastus.monsterin_kolikot}")
        input()
        if vastus.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta.")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

    def taistelu_lohjan_prisma(self, vastus1, vastus2, vastus3):
        print("areena Lohjan prisma!!!")
        input()
        print(f"{self.nimi} vastaan {vastus1.nimi} ja {vastus2.nimi}")
        input()
        print(f"{self.nimi} kolikkomäärä: {self.pelaajan_kolikot} vastustajien kolikkomäärät ovat: {vastus1.monsterin_kolikot} ja {vastus2.monsterin_kolikot}")
        input()
        if vastus3.monsterin_kolikot > self.pelaajan_kolikot:
            print(f"{self.nimi} et selvinnyt tästä alueesta")
            input()
            print("peli päättyy.")
            sys.exit()
        else:
            print(f"{self.nimi} selvisit tästä alueesta.")
            input()
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus1.monsterin_kolikot
            self.pelaajan_kolikot = self.pelaajan_kolikot - vastus2.monsterin_kolikot
            print(f"pelaajan tämänhetkinen kolikkomäärä: {self.pelaajan_kolikot}")
            input()

class Pelaaja(Hahmo):       #tässä luodaan hahmo. nimi ja kolikot peritään Hahmo luokalta
    def __init__(self, nimi, kolikot):
        super().__init__(nimi,kolikot)


    def siirry_areenalle_eka(self, minne):      #alueen valinta

        if minne == "1":
            lapi = range(6)
            for n in lapi:
                print()
            print("..........................................................................................")
            print("valitsit Hämeenlinna.")
            print("sinut siirretään hämeenlinna pizza melodia")
            print("..........................................................................................")
            input()
            print("..........................................................................................")
            print("Pizzeria melodi...")
            print("Yhden erityisen henkilön tykkäämä pizzeria...")
            print("mutta ravintolan edessä on joku epämääräinen henkilö....")
            print("..........................................................................................")
            input()
            self.HML_eka_areena()

        if minne == "2":
            lapi = range(6)
            for n in lapi:
                print()
            print("..........................................................................................")
            print("valitsit Viron")
            print("..........................................................................................")
            input()
            print("..........................................................................................")
            print("sinut siirretään areenalle Tallinna.")
            print("..........................................................................................")
            input()
            self.viro_eka_areena()

        if minne == "3":
            lapi = range(6)
            for n in lapi:
                print()
            print("..........................................................................................")
            print("valitsit avaruus")
            print("..........................................................................................")
            input()
            print("..........................................................................................")
            print("sinut siirretään areenalle mars")
            print("..........................................................................................")
            input()
            self.avaruus_eka_areena()

        if minne == "4":
            lapi = range(6)
            for n in lapi:
                print()
            print("..........................................................................................")
            print("valitsit lohja")
            print("..........................................................................................")
            input()
            print("..........................................................................................")
            print("sinut siirretään areenalle lohjan prisma")
            print("..........................................................................................")
            input()
            self.lohja_eka_areena()

    def HML_eka_areena(self):           #tästä eteenpäin alkaa areenat
        pelaaja1.tulosta_tiedot()
        input()
        hml_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_hml(hml_monsteri)
        self.HML_toka_areena()

    def HML_toka_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty Jukolaan")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("Hämeenlinnan jukola...")
        print("kanattaa olla varovainen...")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        jukola_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_jukola(jukola_monsteri)
        self.HML_kolmas_areena()

    def HML_kolmas_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty katumaan")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("Hämeenlinnan katuma...")
        print("tästä paikasta oli se ylen perjantai dokkari...")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        katuma_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_katuma(katuma_monsteri)
        self.HML_neljas_areena()

    def HML_neljas_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty visamäkeen")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("Hämeenlinnan visamäki...")
        print("täällä on tietyn henkilön rakas lähikauppa...")
        print("täällä tietty henkilö on viettänyt paljon aikaa...")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        visamaki_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_visamaki(visamaki_monsteri)
        print("ONNEKSI OLKOON VOITIT PELIN!!")

    def viro_eka_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty Tallinnan satamaan")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("tallinnan satama...")
        print("se on niin kaunista...")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        satama_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_vanha(satama_monsteri)
        self.viro_toka_areena()

    def viro_toka_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty Vanhaan kaupunkiin")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("viron vanha kaupunki...")
        print("vau.")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        vanha_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_vanha(vanha_monsteri)
        print("ONNEKSI OLKOON VOITIT PELIN!!")

    def avaruus_eka_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty Marsiin")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("mars on toisiksi pienin planeetta meidän aurinkokunnassamme merkuriuksen jälkeen!")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        mars_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_mars(mars_monsteri)
        self.avaruus_toka_areena()

    def avaruus_toka_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty Jupiteriin")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("jupiter on isoin planeetta meidän aurinkokunnassamme!")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        jupiter_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_jupiter(jupiter_monsteri)
        self.avaruus_kolmas_areena()

    def avaruus_kolmas_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty Kuuhun")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("ah kaunis kaunis kuu")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        kuu_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_kuu(kuu_monsteri)
        print("ONNEKSI OLKOON VOITIT PELIN!!")

    def lohja_eka_areena(self):
        print("..........................................................................................")
        print("sinut on siirretty Lohjan prismaan")
        print("..........................................................................................")
        input()
        print("..........................................................................................")
        print("täällä on jotain haisevaa lattialla...")
        print("miten tämä on edes mahdollista...")
        print("..........................................................................................")
        input()
        pelaaja1.tulosta_tiedot()
        input()
        kide_monsteri.monsterin_tiedot()
        kris_monsteri.monsterin_tiedot()
        input()
        pelaaja1.taistelu_lohjan_prisma(kide_monsteri, kris_monsteri, lohja_yhteensa)
        print("ONNEKSI OLKOON VOITIT PELIN!!!")


Paavalikko(pelaajankolikot)     #pääkoodissa päävalikko ensimmäinen asia (koodi kyllä käy kaiken muun ekana läpi)

lapi = range(6)
for n in lapi:
    print()
print("..........................................................................................")
print("peli aloitetaan!")
print("..........................................................................................")

kris_monsteri = Pelaaja("kris", krismonsterinkolikot)       #tästä eteenpäin olioiden luontia ja joitakin inputteja parametreiksi
kide_monsteri = Pelaaja("kide", kidemonsterinkolikot)
lohja_yhteensa = Pelaaja("nothing", prismamonsterinkolikot)
avaruus_hirvio1 = Pelaaja("avaruus monsteri", monsterinkolikot)
tallinnan_monsteri = Pelaaja("mik", tallinnamonsterikolikot)
jukola_monsteri = Pelaaja("normaali random mies", jukolamonsterikolikot)
hml_monsteri = Pelaaja("mare", hmlmonsterikolikot)
katuma_monsteri = Pelaaja("herrasmies", katumamonsterikolikot)
visamaki_monsteri = Pelaaja("asin", visamakimonsterikolikot)
satama_monsteri = Pelaaja("satamamonsteri", satamamonsterinkolikot)
vanha_monsteri = Pelaaja("mikk", vanhakaupunkimonsterinkolikot)
mars_monsteri = Pelaaja("mars monsteri", marsmonsterinkolikot)
jupiter_monsteri = Pelaaja("jupiter monsteri", jupitermonsterinkolikot)
kuu_monsteri = Pelaaja("kuu monsteri", kuumonsterinkolikot)
pelaajan_nimi=input("anna pelaajallesi nimi: ")
valitse_areena = input("Valitse areena mihin haluat mennä ""1""/Hämeenlinna ""2""/Tallinna ""3""/avaruus 4/lohja: ")
pelaaja1 = Pelaaja(pelaajan_nimi, pelaajankolikot)
pelaaja1.siirry_areenalle_eka(valitse_areena)
