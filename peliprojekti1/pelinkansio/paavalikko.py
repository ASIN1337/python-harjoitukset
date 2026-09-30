import pelaaja

class Paavalikko:
    def __init__(self):

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