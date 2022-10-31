import random
from card import Card
from deck import Deck
from bridge_hand import BridgeHand

def main():
    """The main program for testing the classes Card, Deck and BridgeHand."""

    random.seed(10)
    test_cards()

    deck = Deck()
    print("The deck:")
    print(deck)
    deck.shuffle()
    print("The deck after shuffling:")
    print(deck)

    test_hands(deck)
    print("The deck after dealing:")
    print(deck)


def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'S')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card(13, 'H')
    print(card4)
    card5 = Card(1, 'C')
    print(card5)
    card6 = Card('X', 'S')
    print(card6)
    card7 = Card(7, 'X')
    print(card7)
    

def test_hands(deck):
    hands_list = [BridgeHand(), BridgeHand(), BridgeHand(), BridgeHand()]
    print("The hands:")
    print_hands(hands_list)

    deal_hands(deck, hands_list)
    print("The hands after dealing:")
    print_hands(hands_list)


def print_hands(hands_list):
    """Prints each hand in the list."""

    for hand in hands_list:
        print(hand)
    

def deal_hands(deck, hands: list) -> None:
    """Deals cards for the hands."""
    for _ in range(BridgeHand.NUMBER_CARDS):
        for hand in hands:
            hand.add_card(deck.deal())


if __name__ == "__main__":
    main()