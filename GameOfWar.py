import random

# War method

def war():
    table = Game(['Justin', 'Mary'])
    table.deal_cards()
    table.play_all()

# Game Class
class Game:

    def __init__(self, players):
        self.players = [Player(name, PlayPile()) for name in players]
        self.deck = CardDeck()
        self.rounds = 0
    
    def print_underline(self,string, line):
        print('\n{}\n{}'.format(string, line * len(string)))

    def deal_cards(self):
        self.deck.shuffle()
        self.deck.setup_playPiles(self.players)
        for player in self.players:
            player.show_playPile()

    def play_once(self, tied=None):
        if tied is None:
            self.count_round()
        collection = Pile()
        for player in (self.players if tied is None else tied):
            player.drop_card(collection)
            if tied:
                player.drop_bonus(collection, 3)
        winner = collection.winner
        if winner is not None:
            collection.reward(winner)
        else:
            winner = self.play_once(collection.tied)
            collection.reward(winner)
        return winner

    def count_round(self):
        self.rounds += 1
        self.print_underline('Starting round {}'.format(self.rounds), '=')

    def play_all(self):
        while not self.finished:
            self.play_once()
        self.show_winner()

    def show_winner(self):
        for player in self.players:
            if player.playPile.has_cards:
                print()
                print(player.name, 'wins!')
                break

    @property
    def finished(self):
        return sum(bool(player.playPile.cards) for player in self.players) == 1
