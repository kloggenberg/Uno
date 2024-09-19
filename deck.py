from card import Card

class Deck:
    def __init__(self):
        self.colours = ["Yellow", "Green", "Blue", "Red"]
        self.numbers = list(range(0,10))
        self.special_list = ["reverse","+2","skip"]
        self.wild_list = ["wild +4","wild"]
        self.cards = self.make_deck()

    
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
                        self.cards.append(Card(colour,x))
    
        for _ in range(0,4):
            for value in self.wild_list:
                self.cards.append(Card(value=value))      
    
        
    def show_cards(self):
        for card in self.cards:
            print(card.get_card())