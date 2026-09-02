
nimi=input("Anna pelaajan nimi: ")

ikä=int(input("Anna pelaajan ikä: "))

print("nimi: " , nimi  , "ikä: " , ikä)

if ikä < 12:
    print("pelaaja on alaikäinen")

if ikä > 12:
        print("hei!", nimi)
        while True:     
            print("päävalikko")
            komento=input("Anna komento: ")

            if komento == "tarina":
                print("hei!", nimi , "tänään on kiva ja aurinkoinen päivä helsingissä toivottavasti sielläkin on aurinkoista")

            if komento == "lahja":
                print(nimi , "!", "tässä sinulle uusi auto")

            if komento == "lopeta": 
                break
               