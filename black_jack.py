"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card == 'A':
        return 1
    elif card in ['J', 'Q', 'K']:
        return 10
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    face_cards = ['J', 'Q', 'K']
    if card_one in face_cards:
        face_card_one = 10
    elif card_two in face_cards:
        face_card_two = 10
    elif card_one == 'A' or card_two == 'A':
        ace_card = 1


    if card_one > card_two:
        return card_one
    elif card_two > card_one:
        return card_two
    elif card_one == card_two:
        return card_one, card_two
# print(higher_card('A', '5'))


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    face_cards = ['J', 'Q', 'K']
    if card_one in face_cards:
        card_one = 10
    if card_two in face_cards:
        card_two = 10
    if card_one == 'A':
        card_one = 11
    if card_two == 'A':
        card_two = 11
    if type(card_one) == str:
        card_one = int(card_one)
    if type(card_two) == str:
        card_two = int(card_two)

    both_cards_with_11 = (card_one + card_two) + 11

    print(both_cards_with_11)
    if both_cards_with_11 < 21:
        return 11
    elif both_cards_with_11 > 21:
        return 1
    elif both_cards_with_11 == 21:
        return 11



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass
