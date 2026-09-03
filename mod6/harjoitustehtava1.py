import random

summa = 0

kuutiot=int(input("anna arpojen määrä: "))    
for n in range(kuutiot):
    kuutio=list(range(kuutiot))
    kuutio[n] = random.randint(1,6)
    print(kuutio[n])
    summa=summa+kuutio[n]
    print("summa on: ", summa)    
    
