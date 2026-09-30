import os

while True:
    tiedoston_nimi = input("anna tiedoston nimi: ")
    try:
        os.remove(tiedoston_nimi)
        break
    
    except FileNotFoundError:
        print("tiedostoa ei löydy, yritä uudelleen")

