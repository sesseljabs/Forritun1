from lib2to3.pgen2.token import NUMBER
from card import Card


class BridgeHand:
    NUMBER_CARDS = 13
    def __init__(self) -> None:
        '''Creates a hand of 13 blank cards.'''
        self.cards = []
        for i in range(self.NUMBER_CARDS):
            self.cards.append(Card())

    def __str__(self) -> str:
        '''Returns the cards in order'''
        out = ""
        for i in range(len(self.cards)):
            out += str(self.cards[i]) + " "
        return out

    def add_card(self,card) -> None:
        '''Adds the given card to the hand at the first available blank position.'''
        for i in range(len(self.cards)):
            if self.cards[i].is_blank():
                self.cards[i] = card
                break