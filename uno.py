from deck import Deck
from player_tracker import Player_tracker
from player import Player
from discard_pile import Discard

class Uno:   
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.top_card = None
        self.set_up()
    
    def run(self):
        print(f"Top card: {self.top_card.get_card()}")
    
    def set_up(self):
        self.get_number_player()
        self.add_players()
        self.top_card = self.deck.get_top_card()
        
    def get_number_player(self):
        while True:
            try:
                self.number_of_players = int(input("Please enter the number of players (min 2, max 4): "))
                if 2 <= self.number_of_players <= 4:
                    break
                else:
                    print("Please enter a number between 2 and 4.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
    
    def add_players(self):
        for player_number in range(1, self.number_of_players + 1):
            name = input(f"Please enter Player {player_number}'s name: ")
            player_cards = self.deck.deal_cards()
            self.players.append(Player(name, player_cards))
