def numerot(summa):
    yhteensä = 0 
    for n in summa:
        yhteensä = yhteensä + n
    return yhteensä

print(numerot([1,2,3,4,5]))