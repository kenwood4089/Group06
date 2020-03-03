import random

# War method

def war():
    table = Game(['Justin', 'Mary'])
    table.deal_cards()
    table.play_all()

# Player Class

class Player:

    def __init__(self, name, playPile):
        self.name, self.playPile = name, playPile

    def drop_card(self, collection):
        if self.playPile.has_cards:
            collection.add_card(self.playPile.take_top(), self)

    def drop_bonus(self, collection, count):
        collection.add_bonus(self.playPile.cards[:count])
        self.playPile.cards = self.playPile.cards[count:]

    def give_cards(self, cards):
        self.playPile.add_all(cards)

    def show_playPile(self):
        print(str(self.name)+ ' has ' + str(self.playPile))
