import random
from yhteys import database_query

class Game_stats:
    def __init__(self, player_name="Player"):
        self.player = player_name
        self.cash = 5000
        self.points = 0
        self.current_location = "EFHK"
        self.suitcase_location = None
        self.icao = ""
        self.total_distance = 0.0
        self.total_consumption = 0.0
        self.game_over = False
        self.current_city = None
        self.current_country = None


    # ARPOMINEN
    def suitcase(self):
        query = (
            "SELECT airport.ident "
            "FROM airport "
            "JOIN country ON airport.iso_country = country.iso_country "
            "WHERE airport.type = 'large_airport' AND country.continent = 'EU' "
            "AND country.iso_country != 'RU';"
        )
        results = database_query(query)
        icao_list = [
            {
                "icao": row[0]
            }
            for row in results
        ]
        if icao_list:
            self.suitcase_location = random.choice(icao_list)["icao"]
            print(f"Uusi sijainti: {self.suitcase_location}")
        else:
            self.suitcase_location = None

    # LASKEE KM ja CO2 "iha inqeesti"
    def get_distance_to(self, from_icao):
        if not from_icao or not self.current_location:
            return 0.0

        query = (
            f"SELECT ST_Distance_Sphere("
            f"ST_GeomFromText(CONCAT('POINT(', a.longitude_deg, ' ', a.latitude_deg, ')'), 4326), "
            f"ST_GeomFromText(CONCAT('POINT(', b.longitude_deg, ' ', b.latitude_deg, ')'), 4326)) "
            f"FROM airport a, airport b "
            f"WHERE a.ident = '{from_icao}' AND b.ident = '{self.current_location}';"
        )

        results = database_query(query)
        if results and len(results) > 0 and results[0][0] is not None:
            return float(results[0][0])
        return 0.0

    # PELIN LOGIIKKA
    def move(self, icao, municipality=None, country=None):
        if self.game_over:
            return {"status": "ENDED", **self.stats()}

        #SIJAINNIN PÄIVITYS
        prev_location = self.current_location
        self.current_location = icao
        self.icao = icao
        if municipality:
            self.current_city = municipality
        if country:
            self.current_country = country

        # LIPUNHINTA (random joka lento/siirto)
        ticket_cost = random.randint(55, 200)
        self.cash -= ticket_cost
        if self.cash < 55:
            self.cash = 0
            self.game_over = True
            # TALLENTAA TULOKSEN TAULUUN HIGHSCORES
            insert_query = (
                "INSERT INTO highscores (name, points, total_km, total_co2) "
                "VALUES (%s, %s, %s, %s);"
            )
            database_query(insert_query, (self.player, self.points, self.total_distance, self.total_consumption))
            return {**self.stats()}

        # PISTEET
        found = (icao == self.suitcase_location)
        if found:
            self.points += 1
            self.suitcase()

        # KM JA CO2 laskuri
        distance_m = self.get_distance_to(prev_location)
        self.total_distance += float(distance_m) / 1000
        self.total_consumption += (float(distance_m) / 1000) * 0.0002

        # STATUS
        status = "CONTINUE"
        if found:
            status = "CONTINUE"
        if self.game_over:
            status = "END"
        # STATUKSEN ALAUTUS
        return {
            "status": status,
            "ticket_cost": ticket_cost,
            "found": found,
            **self.stats()
        }

    # KOKO LUOKAN STATSIEN PALAUTUS
    def stats(self):
        return {
            "player": self.player,
            "cash": self.cash,
            "points": self.points,
            "location": self.current_city or self.current_location,
            "icao": self.icao,
            "total_distance": self.total_distance,
            "total_consumption": self.total_consumption,
            "game_over": self.game_over,
            "city": self.current_city,
            "country": self.current_country,
            "suitcase": self.suitcase_location
        }

    def game_stats(self):
        return self.stats()