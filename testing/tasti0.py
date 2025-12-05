class Auto: # tämä class
    def __init__(self, rekisteri, huippunopeus): # tämä alustaja
        # ominaisuudet
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000

    def kulje(self, aika):
        self.matka += self.nopeus * aika

auto = Auto("ABC-123", 142) # tämä on olio/object
print (f"Auton tiedot -> Rekisterinumero: {auto.rekisteri}, Huippunopeus {auto.huippunopeus} km/h, Nopeus nyt: {auto.nopeus} km/h.")  # olien ominaisuuksien tulos

print (f"Auton kilometrilukema: {auto.matka} km.")

print(f"Auton uusi nopeus: {auto.nopeus} km/h.")

auto.kulje(1.5)

print (f"Matkan jälkeen uusi kilometrilukema on: {auto.matka} km.")