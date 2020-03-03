import random

# War method

def war():
    table = Game(['Justin', 'Mary'])
    table.deal_cards()
    table.play_all()

# Card Class

class Card:

    SUITE = 'Hearts Diamonds Spades Clovers'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()

    def __init__(self, suite, rank):
        self.suite, self.rank = suite, rank

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suite)

    @property
    def value(self):
        return self.RANKS.index(self.rank)

# main function to start the program

if __name__ == '__main__':
    war()
