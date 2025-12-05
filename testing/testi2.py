class Kirjasto:
    def __init__(self, kirjan_nimi, kirjailija, julkaisuvuosi, sivumäärä):
        self.kirjan_nimi = kirjan_nimi
        self.kirjailija = kirjailija
        self.julkaisuvuosi = julkaisuvuosi
        self.sivumäärä = sivumäärä

    def Kirja(self, uusi_kirja):
        for x in range(uusi_kirja):
            print(self.kirjan_nimi, self.kirjailija,self.julkaisuvuosi, self.sivumäärä)
        return

julkaise = Kirjasto("Uus book", "Huippu writter", 2003, 159)

julkaise.Kirja(6)