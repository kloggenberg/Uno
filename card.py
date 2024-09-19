class Card:
    def __init__(self, colour=None, value=None):
        if colour is not None and value is not None:
            self.colour = colour
            self.value = value
            self.card = (self.colour, self.value)
        elif value is not None:
            self.value = value
            self.card = (self.value)
        else:
            self.card = None
        
    def get_card(self):
        return self.card