nimet= set()

nimi=input("anna  nimi: ")



if nimi not in nimet:
    print("uusi nimi")

if nimi in nimet:
    print("aiemmin syötetty nimi")

nimet.add(nimi)

while nimi != "":
    nimi = input("anna uusi nimi: ")


    if nimi not in nimet:
        print("uusi nimi")


    if nimi in nimet:
        print("aiemmin syötetty nimi")

    nimet.add(nimi)    

    if nimi == "":
        for n in nimet:
            print(n)
