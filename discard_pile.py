from card import Card

class Discard:  
    def __init__(self,defualt_card):
        self.discard_pile = []
        self.add_discard_pile(defualt_card)
    
    
    def add_discard_pile(self,card):
        self.discard_pile.append(card)
        
    
    def show_to_card(self):
        print(self.discard_pile[-1])
        
        
    def clear_discard_pile(self):
        self._discard_pile = []
        
        
    def get_discard_pile(self):
        return self._discard_pile