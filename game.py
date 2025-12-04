import random

class Game:
    def __init__(self,player_name):
        self.player = player_name
        self.cash = 2500
        self.points = 0
        self.current_location = "EFHK"
        self.target_location = "LIRF"
        self.total_distance = 0
        self.total_consumption = 0
        self.game_over = False

    def move(self, ):

