class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value 
        self.card = (colour, value)
    
    
    def get_colour(self):
        return self.colour
    
    
    def get_value(self):
        return self.value
    
    
    def get_card(self):
        return self.card