import mysql.connector

connection = False
while not connection:
    try:
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='megapint',
            password='wine',
            autocommit=True,
            ssl_disabled=True
            )
        connection = True
    except:
        print("\nERR: TARKISTA SYÖTETYT ARVOT")
        connection = False


# Kysely mahdollistaa lisäparametrin käytön ja palauttaa kaikki rivit.
# Jos lisäparametrille ri käyttöä -> palauttaa tyhjän tai tyhjän tuplen
def database_query(query, params=()):
    kursori = yhteys.cursor()
    kursori.execute(query, params)
    return kursori.fetchall()

# arvojen muuttamista varten, ei palauta mitään
def database_update(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    return
# käyttö: jos haluaa vain ensimäisen arvon tulokseen, eli käytettävä vain jos haluaa yhden arvon
def database_query_fetchone(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchone()
    return tulos
# kysely jos on tarvetta tarkistaa löytyykö tieto esim
def database_check_query(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return True
    else:
        return False
