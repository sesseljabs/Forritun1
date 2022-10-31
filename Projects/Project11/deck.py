import random
from card import Card

class Deck:
    def __init__(self) -> None:
        '''Creates a deck of 52 cards'''
        self.cards = []
        for suit in ['S','H','D','C']:
            for rank in range(1,14):
                self.cards.append(Card(rank,suit))
    
    def __str__(self) -> str:
        '''Prints all cards in a row with break after 13 cards.'''
        out = ""
        for i in range(len(self.cards)):
            out += str(self.cards[i]) + " "
            if (i+1) % 13 == 0 and i < len(self.cards)-13:
                out += "\n"
        return out

    def shuffle(self) -> None:
        '''Shuffles the cards in the deck.'''
        random.shuffle(self.cards)

    def deal(self) -> Card:
        '''Deals a single card from the deck by returning the card removed from the top of the deck.'''
        return self.cards.pop(0)