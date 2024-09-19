class Player_tracker:
    def __init__(self,number_of_players):
        self.number_of_players = list(range(0,number_of_players))
        print(self.number_of_players)
        
        
    # def show_players(self):
    #     for index, player in enumerate(self.number_of_players):
    #         print()
    #     pass
    
    
    def reverse_players(self):
        self._player_tracker.reverse()
        
        
    def remove_player(self, player):
        self._player_tracker.remove()