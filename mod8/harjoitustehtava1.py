vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero: "))



if kuukausi == 12 or 1 <= kuukausi < 3:
    print("kuukausi on", vuodenajat[0])

elif 3 <= kuukausi < 6:
    print("kuukausi on", vuodenajat[1])

elif 6 <= kuukausi <= 8:
    print("kuukausi on", vuodenajat[2])

elif 9 <= kuukausi <= 11:
    print("kuukausi on", vuodenajat[3])