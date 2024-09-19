class Player:
    def __init__(self,name,cards):
        self.name = name
        self.cards = cards

        
    def remove_card(self,card):
        self.cards.remove(card)
    
    
    def add_cards(self,card):
        self.cards.append(card)

        
    def get_cards(self):
        return self.cards
    

    def show_player_info(self):
        print(f"Player {self.name}:")
        for index ,card in enumerate(self.cards):
            print(f"Card {index+1} : {card.get_card()}")
            
            
    def say_uno(self):
        print("UNO!!!")