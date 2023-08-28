class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach


    def get_player_name(self):
        return self.name
    
    def get_players(self):
        return self.players
    
    def get_coach(self):
        return self.coach
    
    def add_player(self, input_name):
        return self.players.append(input_name)
    
    def has_player(self, player_name):
        for player in self.players:
            if player_name == player:
                return True
        return False
    
    
