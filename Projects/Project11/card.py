
SUITS = ['H','S','D','C']
NUM_CARDS = ['A','J','Q','K']

class Card:
    def __init__(self,rank=0,suit="") -> None:
        '''Converts rank character or integer into an integer range 1-13'''
        if type(rank) == int:
            self.rank = rank
        elif type(rank) == str and rank in NUM_CARDS:
            if rank == "A":
                self.rank = 1
            elif rank == "J":
                self.rank = 11
            elif rank == "Q":
                self.rank = 12
            elif rank == "K":
                self.rank = 13
            else:
                self.rank = int(rank)
        else:
            self.rank = 0

        '''Makes suit character blank if not in SUITS'''
        if type(suit) == str:
            if suit in SUITS:
                self.suit = suit
            else:
                self.suit = ""
        else:
            self.suit = ""

    def __str__(self) -> str:
        '''Returns card rank and suit as a string'''
        retstr = ""
        if self.rank == 0 or self.suit == "":
            return "blk"
        elif self.rank == 1:
            retstr += "A"
        elif self.rank == 11:
            retstr += "J"
        elif self.rank == 12:
            retstr += "Q"
        elif self.rank == 13:
            retstr += "K"
        else:
            retstr += str(self.rank)
        retstr += self.suit
        return f"{retstr:>3}"

    def is_blank(self) -> bool:
        '''Returns true if a card is blank, otherwise false'''
        if self.rank == 0:
            return True
        else:
            return False