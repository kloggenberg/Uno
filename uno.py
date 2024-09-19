from deck import Deck
from player_tracker import Player_tracker
from player import Player

class Uno:   
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.set_up()
    
    
    def run(self):
        self.add_players()
        pass
    
    
    def set_up(self):
        self.get_number_player()
        pass
        
        
    def get_number_player(self):
        while True:
            try:
                self.number_of_players = int(input("Please enter the amount of players (min 2 player and max number of players is 4): "))
                if 2 <= self.number_of_players <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
                
    
    def add_players(self):
        for player_number in range(1,self.number_of_players+1):
            name = input(f"Please enter Player {player_number} name: ")
            player_cards = self.deck.deal_cards()
            # player = 
            self.players.append(Player(name,player_cards))
            
