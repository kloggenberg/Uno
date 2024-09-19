from card import Card

class Discard:  
    def __init__(self):
        self.discard_pile = []
    
    
    def add_discard_pile(self,card):
        self.discard_pile.append(card)
        
    
    def show_to_card(self):
        print(self.discard_pile[-1])
        
        
    def clear_discard_pile(self):
        self._discard_pile = []