# game.py
import random

class Game_stats:
    def __init__(self, player_name="Player"):
        self.player = player_name
        self.cash = 2500
        self.points = 0
        self.current_location = "EFHK"   # start HEL (ICAO)
        self.suitcase_location = "LIRF"  # Rome example
        self.icao = ""
        self.weather = ""
        self.total_distance = 0.0
        self.total_consumption = 0.0
        self.game_over = False

    def move(self, icao_code, distance_m):
        if self.game_over:
            return {"status": "ENDED", "message": "Game already over.", **self.game_stats()}

        ticket_cost = random.randint(55, 200)


        self.current_location = icao_code
        self.icao = icao_code
        self.total_distance += float(distance_m)

        self.total_consumption += float(distance_m) * 0.0002

        self.cash -= ticket_cost
        if self.cash < 0:
            self.cash = 0

        found = False
        if icao_code == self.suitcase_location:
            self.points += 1
            found = True

        if self.cash <= 0:
            self.game_over = True
            status = "LOSE"
            message = "Out of money."
        elif found:
            status = "WIN"
            message = "You found the suitcase!"
        else:
            status = "OK"
            message = "Moved."

        return {
            "status": status,
            "message": message,
            "ticket_cost": ticket_cost,
            "cash": self.cash,
            "points": self.points,
            "location": self.current_location,
            "icao": self.icao,
            "weather": self.weather,
            "total_distance": self.total_distance,
            "total_consumption": self.total_consumption,
            "game_over": self.game_over
        }

    def game_stats(self):
        return {
            "player": self.player,
            "cash": self.cash,
            "points": self.points,
            "location": self.current_location,
            "suitcase": self.suitcase_location,
            "icao": self.icao,
            "weather": self.weather,
            "total_distance": self.total_distance,
            "total_consumption": self.total_consumption,
            "game_over": self.game_over
        }

    def new_suitcase_location(self):
        return self.suitcase_location