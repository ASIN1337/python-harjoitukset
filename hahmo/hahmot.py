'''
1. Lue koodi läpi, suorita se, varmista että ymmärrät, miten se toimii nyt.
2. Luo luokat Hirvio ja Pelaajahahmo. Ne molemmat perivät luokan Hahmo.
3. Muokkaa koodia niin, että lisäät Pelaajahahmo-luokalle ominaisuuden tavaralista. 
Kun pelaajahahmo-olio luodaan, se saa parametrinä listan tavaroita, jotka tallennetaan olion listaan.
4. Ylikirjoita Hahmo-luokan tulosta-metodi Pelaajahahmolle niin, että se tulostaa mukaan myös tavaralistan.
5. Muokkaa niin, että vain hirviöillä on repliikki, ei kaikilla Hahmo-olioilla.
6. Ylikirjoita Hirvio-luokan tulosta-metodi niin, että se tulostaa myös repliikin.
7. Jos ehdit: Luo peliin useampi hirviö, ja laita pelaajahahmo taistelemaan myös niiden kanssa. 
Taistelu-metodia ei tarvita sekä hahmolle että hirviölle. 
Siirrä se sille luokalle, jossa se on sinusta looginen. 
Testaa, että peli toimii järkevästi.
'''

class Hahmo:
    def __init__(self, nimi, repliikki):
        self.nimi = nimi
        self.repliikki = repliikki
        self.hp = 100

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")


    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        input()
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            self.tulosta_tiedot()

#class Hirvio(Hahmo):


class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, repliikki, inventory):
        self.inventory = inventory
        self.inventory = []
        self.inventory.append(inventory)   
        super().__init__(nimi, repliikki)     

merihirvio = Hahmo("Merihirviö", "Lits läts, aion syödä sinut!")
pelaajahahmo = Hahmo(input("Anna hahmon nimi: "), "Olen sankari ja voitan kaikki!")


print("Peli alkaa.")
pelaajahahmo.tulosta_tiedot()
input()

print(f"{pelaajahahmo.nimi} kohtaa ensimmäiseksi kauhean hirviön. Hirviö huutaa:")
print(merihirvio.repliikki)
merihirvio.tulosta_tiedot()

input()
pelaajahahmo.taistelu(merihirvio)
input()
print(f"Peli ohi.")






