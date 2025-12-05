year = int(input("Syötä vuosiluku: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Syöttäväsi vuosiluku: " + str(year) + " on karkausvuosi")

else:
    print(str(year) + " ei ole karkausvuosi.")

####################################################################################

number = 1
while number <= 1000:
   if number % 3 == 0:
       print(number)
   number = number + 1

####################################################################################

print ("Muunna tuumat -> senttimetreiksi.")
value = 0
while value >= 0:
    value = float(input("Syötä tuumien määrä: "))
    number = value * 2.54
    print(str(number) + "tuumaa.")
    if value < 0:
        break

####################################################################################

print ("Arvaa numero väliltä 1-10")
import random
secret_number = random.randint(1, 10)

while True:
    arvaus = input("Syötä uusi numero: ")
    arvaus = int(arvaus)

    if arvaus == secret_number:
        print ("Oikein!")
        break

    elif arvaus < secret_number:
        print ("Väärin, luku on suurempi. Arvaa uudestaan!")
    elif arvaus > secret_number:
        print ("Väärin, luku on pienempi. Arvaa uudestaan!")

####################################################################################
print ("Ohjelma laskee π:n likiarvon generoimien satunnaispisteiden avulla.")
while True:
    shots = input("Syötä pisteiden määrä: ")
    N = int(shots)  # pisteet
    if N < 1 or N > 10000000:
        print("Virheellinen luku, syötä arvo 1 ja 10 milj. välillä.")
    else:
        break
# While True loop: pitää huolen että numero on 1-10milj välillä toimivuuden takaamiseksi.
# N = int(shots) muuttaa syötetyn arvon pythonille ymmerrättäväksi kokonaisluvuksi

n = 0 # osumat
import random
for pisteet in range(N): # range funtio eli listan läpikäynti
    x = random.uniform(-1, 1) #sattumanvarainen murtoluku -1  ja 1 väliltä
    y = random.uniform(-1, 1) #sattumanvarainen murtoluku -1  ja 1 väliltä

    if x**2 + y**2 < 1: # TESTIKAAVA: Jos toteutuu ypäyhtälö x^2+y^2<1 = kyseessä on osuma
        n = n + 1 # Mikäli osuma -> muuttuja "n" arvoa nostetaan +1:llä

likiarvo = 4 * n / N # Kaava likiarvon laskemiseen = π≈4n/N
likiarvo = float(likiarvo)
print ("Pii:n likiarvo: " + str(likiarvo))

####################################################################################
import random

numbers = []
for x in range(numbers): # x on loopin toimivuutta varten
    number = random.randint(1, 6)
    numbers.append(number)

print (numbers)

####################################################################################
numerolista = []

while True:
    numero = input("Syötä uusi numero: ")
    if numero == "":
        break
    else:
        numero = int(numero)
        numerolista.append(numero) # nostaa ja tallentaa numeron numerolistaan

numerolista.sort(reverse=True)

print (numerolista)

####################################################################################

kaupungit = []

for x in range (5):
    kaupunki = input("Kaupunki: ")
    kaupungit.append(kaupunki)

print (kaupungit)

####################################################################################

import random

def parametriton():
    while True:
        nopanheitto = random.randint (1, 6 )

        if nopanheitto == 6:
            print(str(nopanheitto) + " -> Sä osuit!")
            break
        else:
            print ("Heitit: " + str(nopanheitto) + ":n")

parametriton()

####################################################################################

print("Ohjelma listan numerot yhteen.")

numerolista = [5, 11, 2, 18, 24, 19]

def laskekaikki(numerolista): # funktio näkee koko listan ja kiakki sen arvot
    summa = 0
    for i in numerolista: # python automaattisesti menee numerolistan läpi
        summa = summa + i
        print("- " + str(i))
    return summa

yht = laskekaikki(numerolista)
print("Listassa olevien numeroiden summa on: ", yht)

####################################################################################

def alikaks(parilliset):
    print(parilliset)

def aliyks(kaiqqinum):
    print(kaiqqinum)
    alikaks(parilliset)

print ("Ohjelma tulostaa 2x listaa. Kaikki / vain parittomat numerot.")

kaiqqinum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
parilliset = [2,4,6,8,10,12,14,16,18,20]


aliyks(kaiqqinum)

####################################################################################

def hae_tiedot(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"KAUPUNKI: {rivi[0]}, KUNTA: {rivi[1]}")
    else:
        print("Kyseisellä ICAO-koodilla ei löytynyt tietoja.")
    kursori.close()

print ("Ohjelma hakee ICAO-koodilla lentokentän tiedot.")
icao = input(str("ICAO koodi:"))
hae_tiedot(icao)

####################################################################################

import mysql.connector
from collections import Counter # LISÄTTY. Python moduuli joka tehty erinäisen datan laskemiseen.
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='wine',
         autocommit=True
         )

def hae_tiedot(iso_country):
    sql = f"SELECT name, type FROM airport WHERE iso_country = '{iso_country}'" # TOIMII
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    # if kursori.rowcount >0 :  -> else: lopussa ajaa samaa kuin tämä rivi
    if tulos:
        tyypit = Counter() # LISÄTTY -> tavallinen functio laskisi vaan yhteen kaikki tyypit.
        # Counter taas on sisäänrakennettu functio, joka osaa myös erottamaa eri tyyppien tosistaan
        # ja laskee ne erillisinä samaan tapaan kuten kirjastolista. Eli sillä on "dictionary" tyyppinen rakenne,
        # jossa eri tyyppi on eri "KEY".
        for rivi in tulos: #looppi printtaa kaikki kentät. Samalla rivillä tiedot: nimi + tyyppi
            print(f"LENTOKENTTÄ: {rivi[0]}, TYYPPI: {rivi[1]}")
            tyypit[rivi[1]] += 1 # laskuri -> kpl määrät
        print("===============================================================") # printtauksessa erottelee tiedon
        for airport_type, count in tyypit.items():
            print(f"{count} {airport_type}(s)")
    else:
        print("Kyseisellä maakoodilla ei löytynyt tietoja.")

    kursori.close()

print ("Ohjelma etsii maakoodilla kaikki sen lentokentät (esim. FI).")
iso_country = input("Syötä maakooodi: ").upper() # LISÄTTY .upper() -> muuttaa kirjaimet isoksi "toimintavarmempi"
hae_tiedot(iso_country)
####################################################################################

def calculate_distance(icao1, icao2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident IN ('{icao1}', '{icao2}')"
   # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if len(tulos) != 2:
        print("Virhe, yhtä tai molempiä kenttiä ei löytynyt.")
        return

    #lat1, lon1 = tulos[0]
    #lat2, lon2 = tulos[1]
    #icao1_coords = (lat1, lon1)
    #icao2_coords = (lat2, lon2)
    # etaisyys = distance(icao1_coords, icao2_coords).kilometers
    etaisyys = distance(tulos[0], tulos[1]).kilometers

    print(f"Etäisyys {icao1} ja {icao2} välillä on {etaisyys:.2f} kilometriä.")

print ("Ohjelma laskee kahden lentokentän etäisyyden ICAO koodien aculla.")
icao1 = input("Syötä ensimmäinen ICAO:")
icao2 = input("Syötä toinen ICAO:")

calculate_distance(icao1, icao2)

####################################################################################

def luo_autot():
    autot = []
    merkit = ["Toyota", "Mercedes", "BMW", "Audi", "Ford", "Chevrolet", "Honda", "Nissan", "Porsche", "Volkswagen"]
    for i in range(1, 11):
        name = random.choice(merkit)
        merkit.remove(name)
        rekisteri = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippunopeus, name))
    return autot

autot = luo_autot()

####################################################################################


####################################################################################

def aliyks():
    while True:
        icao = input("Syötä nelikirjaiminen ICAO:")
        if icao == "":
            print("Virheellinen koodi. Ohjelma loppu")
            break
        if icao in lennot:
            print(f"{icao} {lennot[icao]}")
        else:
            print(f"Kyseiseklä koodilla: {icao} ei löytynyt tietoja.")


# LISÄÄMINEN
def alikaks():
    while True:
        koodi = input("Syötä uuden kaupungin ICAO: ")
        if koodi == "":
            print("Ohjelma loppu.")
            break

        if koodi in lennot:
            print (f" Koodi: {koodi} löytyy jo. ")
        else:
            kaupunki = input("SSyötä uusi kaupunki: ")


print ("OHJELMA1: VALITSE TOIMINTO:")
print ("[1] = HAE LENTOKENTÄN TIEDOT: ICAO-koodilla")
print ("[2] = LISÄÄ UUSI LENTOKENTTÄ")
print ("[ENTER] = LOPETA OHJELMA")


while True:
    valinta = input("Syötä valinta:")

    if valinta == "":
        print ("Ohjelma loppu.")
        break

    valinta = int(valinta)

    if valinta == 1:
         print("Ohjelma1: Hae haluamasi lentokentän tiedont ICAO-koodillaa:")
         aliyks()

    elif valinta == 2:
         print("Ohjelma2: Lisää uusia Kaupunkeja ICAO koodin avulla:")
         alikaks()

    else:
         print("Virheellinen valinta! Syötä luku 1, 2 tai paina enter.")

####################################################################################
print ("Ohjelma valitsee syötetyistä arvoista pienimmän ja suurimman.")
print ("Lopeta ohjelma painamalla enter.")

pienin_numero = None
suurin_numero = None

while True:
    new_number = input ("Syötä uusi numero: ")
    if new_number == "":
        break

    new_number = float(new_number)

    if pienin_numero is None or new_number < pienin_numero:
        pienin_numero = new_number
    if suurin_numero is None or new_number > suurin_numero:
        suurin_numero = new_number

pienin_numero = int(pienin_numero)
suurin_numero = int(suurin_numero)

print ("Numero " + str(pienin_numero) + " oli pienin syöttämäsi numero.")
print ("Numero " + str(suurin_numero) + " oli suurin syöttämäsi numero.")

####################################################################################

