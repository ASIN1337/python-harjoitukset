lukuja= []



while True:
    luku=(input("anna numero: "))
    if luku == "":
        break

    lukuja.append(luku)
    lukuja.sort(key=float, reverse=True)

    uusi_lukuja=[float(luku) for luku in lukuja]

print(uusi_lukuja[0:5])
