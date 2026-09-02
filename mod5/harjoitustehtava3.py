suurin = 0
pienin = 0

while True:
    lukuja=(input("Anna luku: "))
    if lukuja == "":
        break

    lukuja = float(lukuja)

    if suurin == 0 or lukuja >= suurin:
        suurin = lukuja
    else:
        suurin = suurin

    if pienin == 0 or lukuja <= pienin:
        pienin = lukuja
    else:
        pienin = pienin

print("suurin on", suurin)
print("pienin on", pienin)


