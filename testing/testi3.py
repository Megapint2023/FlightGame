# LUOKKAMUUTTUJA (staattinen muuttuja)

class Auto: # LUOKKA

    kierros = 0 # LUOKKAMUUTTUJA (staattinen muuttuja)

    def __init__(self, merkki, vuosimalli, lap="Hep!"): # ALUSTAJA
        self.merkki = merkki # ATRIBUUTTI
        self.vuosimalli = vuosimalli # ATRIBUUTTI
        self.lap = lap # ATRIBUUTTI
        Auto.kierros = Auto.kierros + 1 # STAATTINEN MUUTTUJA (staattinen muuttuja)

auto1 = Auto("Mersu", 2018) # OLION luominen
auto2 = Auto("BMW", 2022, "Yo!") # OLION LUOMINEN
auto3 = Auto("Audi", 2000, "GG!") # OLION LUOMINEN
print (f"Kierroksia ajettu nyt: {Auto.kierros}.")



class Auto:
    def __init__(self, merkki, malli, rekkari, ilmoitus = "NEW LAP!"):
        self.merkki = merkki
        self.malli = malli
        self.rekkari = rekkari
        self.ilmoitus = ilmoitus

    def kierros(self, x):
        for i in range(x):
            print(self.merkki, self.malli, self.rekkari)
        return

auto1 = Auto("Mersu", "C", 678)
auto2 = Auto("BMW", "X", 578)

auto1.kierros(5)
auto2.kierros(4)






















