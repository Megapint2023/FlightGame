import random
from yhteys import database_query

class Game_stats:
    def __init__(self, player_name="Player"):
        self.player = player_name
        self.cash = 2500
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
    def randomize_suitcase(self):
        """
        Pick a random ICAO from the same airport set we show on the map
        (large EU airports, excluding RU). Sets self.suitcase_location.
        """
        query = (
            "SELECT airport.ident "
            "FROM airport "
            "JOIN country ON airport.iso_country = country.iso_country "
            "WHERE airport.type = 'large_airport' AND country.continent = 'EU' "
            "AND country.iso_country != 'RU';"
        )
        rows = database_query(query)
        icaos = [r[0] for r in rows] if rows else []
        if icaos:
            self.suitcase_location = random.choice(icaos)
            print(f"New suitcase location: {self.suitcase_location}")
        else:
            self.suitcase_location = None
            print("Warning: no airports found for suitcase randomization.")

    # TARKISTA / KORJAA / KYSY
    def move(self, icao, distance_m, municipality=None, country=None):
        if self.game_over:
            return {"status": "ENDED", **self.stats()}

        #SIJAINNIN PÄIVITYS
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
            return {
                "status": "LOSE",
                "message": "Not enough cash to fly.",
                **self.stats()
            }
        # PISTEET
        found = (icao == self.suitcase_location)
        if found:
            self.points += 1
            self.randomize_suitcase()

        # KM JA CO2 laskuri
        self.total_distance += float(distance_m)
        self.total_consumption += float(distance_m) * 0.0002

        # STATUS
        status = "OK"
        if found:
            status = "WIN"
        if self.game_over:
            status = "END"
        # PALAUTUS
        return {
            "status": status,
            "ticket_cost": ticket_cost,
            "found": found,
            **self.stats()
        }

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