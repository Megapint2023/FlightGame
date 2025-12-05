class Koira:                                                     # LUOKKA
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"): # ALUSTAJA = KONSTRUKTORI (luo attribuutit)
        self.nimi = nimi                                         # OLION ATTRIBUUTTI
        self.syntymävuosi = syntymävuosi                         # OLION ATTRIBUUTTI
        self.haukahdus = haukahdus                               # OLION ATTRIBUUTTI

    def hauku(self,kerrat):                                      # METODI
        for i in range(kerrat):                                  # TOISTORAKENNE / LOOPPI
            print(self.haukahdus)                                # METODIN TOIMINTO
        return                                                   # PALAUTUS

koira1 = Koira("Aapo", 2018)                    # OLION LUONTI
koira2 = Koira("Koira", 2022, "Hau")  # OLION LUONTI

koira1.hauku(2)                                                   # METODIKUTSU
koira2.hauku(5)                                                   # METODIKUTSU


class Auto: # LUOKKA
    def __init__(self, merkki, väri, vuosi, kierros="Lap completed!"): # ALUSTAJA
        self.merkki = merkki # ATTRIBUUTTI
        self.väri = väri # ATTRIBUUTTI
        self.vuosi = vuosi # ATTRIBUUTTI
        self.kierros = kierros # ATTRIBUUTTI

    def ilmoitus(self, lap): # METODI
        for i in range(lap): # LOOPPI
            print(self.kierros)
        return # PALAUTUS

auto1 = Auto("Mersu", "punainen", 2000)
auto2 = Auto("Audi", "sininen", 1999)

auto1.ilmoitus(6)
auto2.ilmoitus(9)




class Weapon: # LUOKKA
    def __init__(self, kind, weight, damage, sound = "DAMAGE DONE"): # ALUSTAJA (kostruktori)
        self.kind = kind # ATTRIBUUTTI (käyttö: tiedon tallentaminen olioon)
        self.weight = weight # ATTRIBUUTTI
        self.damage = damage # ATTRIBUUTTI
        self.sound = sound # ATTRIBUUTTI

    def turn(self, x): # METODI
        for i in range (x): # LOOP
            print(self.damage, self.sound) # METODIN TOIMINTO
        return # PALAUTUS

player1 = Weapon("axe", "12kg", 3) # OLION LUOMINEN
player2 = Weapon("mace", "10kg", 2.5) # OLION LUOMINEN

player1.turn(2) # METODIKUTSU
player2.turn(2) # METODIKUTSU

# HARJOITUS
class Pistooli:
    def __init__(self, merkki, valmistusvuosi, ikä, ääni= "BAM!" ):
        self.merkki = merkki
        self.valmistusvuosi = valmistusvuosi
        self.ikä = ikä
        self.ääni = ääni

    def panos(self, x):
        for i in range(x):
            print(self.merkki, self.valmistusvuosi, self.ikä)
        return

pistooli1 = Pistooli("Cold", 1922, 12)
pistooli2 = Pistooli("Magnum", 1875, 69)

pistooli1.panos(4)
pistooli2.panos(2)



















