import random

nimi=input("Anna pelaajan nimi: ")

ikä=int(input("Anna pelaajan ikä: "))

print("nimi: " , nimi  , "ikä: " , ikä)

esineet=[]

def kysy_esine():
        kysymys = input ("anna pelaajalle esine tai lopeta painamalla enter: ")
        esineet.append(kysymys)
        print("pelaaja on saanut esineen", kysymys)
        while kysymys != "":
            kysymys = input("anna pelaajalle uusi esine tai lopeta painamalla enter: ")
            esineet.append(kysymys)
            print("pelaaja on saanut esineen", kysymys)
        
def gifting():
        giftrandom=(random.randint(1,2))
        if giftrandom == 1:
             print("olet saanut lahjasta hatun")
             esineet.append("hattu")
        if giftrandom == 2:
             print("olet saanut lahjasta lemmikki lohikäärmeen")
             esineet.append("lohikäärme miku")

     

def listan_sisalto():
     print("näytetään pelaajalle tavaraluettelo")
     print(esineet)



if ikä < 12:
    print("pelaaja on alaikäinen")

if ikä >= 12:
        print("hei!", nimi)
        while True:     
            print("päävalikko!!")
            print("kirjoita joko " "esine"", ""tavaraluettelo"", ""lahja"" tai lopeta")
            komento=input("Anna komento: ")

            if komento == "esine":
                kysy_esine()
                

            if komento == "lahja":
                gifting()

            if komento == "tavaraluettelo":
                 listan_sisalto()

            if komento == "lopeta": 
                break

