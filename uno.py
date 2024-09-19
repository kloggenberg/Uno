from deck import Deck
from player_tracker import PlayerTracker
class Uno:   
    def __init__(self):
        pass
    
    
    def run(self):
        players = PlayerTracker(4)
        
    
    def set_up(self):
        number_of_players = input("Please enter the amount of players (max number of players is 4):")
        print(number_of_players)