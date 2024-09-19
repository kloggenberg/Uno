import os
import platform

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
        self.clear_screen()
        
        for player in self.players:
            self.get_player_input(player)            
    
    
    def check_card_playable(self, card):
        """Check if the selected card is playable based on the top card."""
        if card.get_card()[0] == "Wild":
            # Wild cards are always playable
            return True
        elif card.get_card()[0] == self.top_card.get_card()[0]:
            # Check if colors match
            return True
        elif card.get_card()[1] == self.top_card.get_card()[1]:
            # Check if numbers or special values match
            return True
        return False
    
    
    def get_player_input(self, player):
        while True: 
            try:
                print(f"Top card : {self.top_card.get_card()}")
                
                print(f"\n{player.get_player_name()}'s turn:")
                player.show_player_info()  # Display player's hand
                
                # Prompt the player to select a card to play
                user_input = int(input("Please enter the card number you want to play (or 0 to draw a card): "))
                
                if 0 <= user_input <= len(player.get_player_cards()):
                    if user_input == 0:
                        print("Player wants to draw a card")
                        # TODO: Implement logic to draw a card
                        break
                    else:
                        selected_card = player.get_player_cards()[user_input - 1]
                        
                        # Check if the selected card is playable
                        if self.is_playable(selected_card):
                            print(f"Playing card: {selected_card.get_card()}")
                            player.remove_card(selected_card)  # Remove card from player's hand
                            self.top_card = selected_card  # Update top card
                            
                            if len(player.get_player_cards()) == 1:
                                player.say_uno()  # Player should say UNO if only one card is left
                            
                            break
                        else:
                            print("That card is not playable. Please choose another card.")
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
           
           
            
    def is_playable(self, card):
        # Check if the card is a Wild card or matches the top card's color or value
        if card.get_card()[0] == "Wild":
            return True
        if card.get_card()[0] == self.top_card.get_card()[0]:  # Check color match
            return True
        if card.get_card()[1] == self.top_card.get_card()[1]:  # Check value match
            return True
        return False


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


    def clear_screen(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')