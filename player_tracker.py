class Player_tracker:
    def __init__(self,number_of_players):
        self.number_of_players = list(range(1,number_of_players+1))
        print(self.number_of_players)
    
    
    def reverse_players(self):
        self._player_tracker.reverse()
        
        
    def remove_player(self, player):
        self._player_tracker.remove()