from hahmoluokat1 import Hahmo, Hirvio, Pelaajahahmo


merihirvio = Hirvio("Merihirviö", "Lits läts, aion syödä sinut!", 10)
pelaajahahmo = Pelaajahahmo(input("Anna hahmon nimi: "), 100, ["miekka", "kilpi"])

pelaajahahmo.tulosta_tiedot()

print(f"{pelaajahahmo.nimi} kohtaa ensimmäiseksi kauhean hirviön.")
merihirvio.tulosta_tiedot()
input()
pelaajahahmo.taistelu(merihirvio)