import random

# War method

def war():
    table = Game(['Justin', 'Mary'])
    table.deal_cards()
    table.play_all()

# Pile Class

class Pile:

    def __init__(self):
        self.cards = []
        self.players = []
        self.bonus = []

    def add_card(self, card, player):
        self.cards.append(card)
        self.players.append(player)

    def add_bonus(self, cards):
        self.bonus.extend(cards)

    @property
    def winner(self):
        self.show_pile()
        values = [card.value for card in self.cards]
        self.best = max(values)
        if values.count(self.best) == 1:
            return self.players[values.index(self.best)]

    def show_pile(self):
        for player, card in zip(self.players, self.cards):
            print('{} laid down a {}.'.format(player.name, card))

    def reward(self, player):
        player.give_cards(self.cards)
        player.give_cards(self.bonus)

    @property
    def tied(self):
        for card, player in zip(self.cards, self.players):
            if card.value == self.best:
                yield player


# CardDeck Class

class CardDeck:

    def __init__(self):
        self.cards = [Card(s, r) for s in Card.SUITE for r in Card.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def setup_playPiles(self, players):
        playPiles = [player.playPile for player in players]
        while len(self.cards) >= len(players):
