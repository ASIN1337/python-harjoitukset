vuosi=int(input("Anna vuosiluku: "))

karkausvuosi=vuosi % 4

if karkausvuosi == 0:
    if karkausvuosi % 100  == 0:
        if karkausvuosi % 400 == 0:
            print("vuosi on karkausvuosi")

        else:
            print("vuosi ei ole karkausvuosi")        
    else:
        print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")        