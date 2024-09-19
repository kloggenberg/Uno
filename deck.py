import random
from card import Card

class Deck:
    def __init__(self):
        self.NUMBER_OF_CARDS_PER_HAND = 7
        self.colours = ["Yellow", "Green", "Blue", "Red"]
        self.numbers = list(range(0,10))
        self.special_list = ["reverse","+2","skip"]
        self.wild_list = ["+4","basic"]
        self.cards = []
        self.make_deck()
        self.shuffle_deck()


    def get_deck(self):
        return self.cards
    
    def get_top_card(self):
       return (self.cards.pop(0))
    
    def make_deck(self):
        for colour in self.colours:
            for number in self.numbers:
                if number == 0:
                    self.cards.append(Card(colour,number))
                else:
                    for _ in range(0,2): 
                        self.cards.append(Card(colour,number))
            for x in self.special_list:
                    for _ in range(0,2):
                        self.cards.append(Card(colour,number))
        
        for _ in range(0,4):
            for value in self.wild_list:
                self.cards.append(Card("Wild",value))      
    
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
        
        
    def show_cards(self):
        for card in self.cards:
            print(card.get_card())
            
    
    def deal_cards(self):
        player_hand = []
        for _ in range(0,7):
            player_hand.append(self.cards.pop(0))
        return player_hand
    
    
    def remake_deck(self):
        pass