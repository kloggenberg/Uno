class Player:
    def __init__(self,name,cards):
        self.name = name
        self.cards = cards
        self.still_playing = True
        
        
    def set_playing(self,playing):
        self._playing = playing
        
        
    def get_player_name(self):
        return self.name
    
    
    def get_player_cards(self):
        return self.cards
    
    
    def remove_card(self,card):
        self.cards.remove(card)
    
    
    def add_cards(self,card):
        self.cards.append(card)

        
    def get_cards(self):
        return self.cards
    

    def show_player_info(self):
        for index ,card in enumerate(self.cards):
            print(f"Card {index+1} : {card.get_card()}")
            
            
    def say_uno(self):
        print("UNO!!!")