leiviskaint=input("Anna leiviskat: ")
naulatint=input("Anna naulat: ")
luoditint=input("Anna luodit: ")
naula1=int(naulatint)
leiviska1=int(leiviskaint)
luoti1=float(luoditint)
luotiperus=13.3
leiviska1=leiviska1 * 13.3 * 52
naula1=naula1 * 13.3 * 32
luoti1=luoti1 * 13.3
gramma=leiviska1 + naula1 + luoti1 
kilo=gramma / 1000
print("massa nykymittojen mukaan: ")
print(kilo , "kilogrammaa", gramma , "grammaa")