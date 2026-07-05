"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    if card in {"K", "Q", "J"}:
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    new_card_one = card_one
    new_card_two = card_two

    if new_card_one in {"K", "J", "Q"}:
        new_card_one = 10
    elif new_card_one == "A":
        new_card_one = 1
    else:
        new_card_one = int(card_one)

    if new_card_two in {"K", "J", "Q"}:
        new_card_two = 10
    elif new_card_two == "A":
        new_card_two = 1
    else:
        new_card_two = int(card_two)

    if new_card_one == new_card_two:
        return card_one, card_two
    
    if new_card_one > new_card_two:
        return card_one
    
    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    if card_one == "A" or card_two == "A":
        return 1

    if card_one in {"K", "Q", "J"}:
        card_one = 10
    else:
        card_one = int(card_one)

    if card_two in {"K", "Q", "J"}:
        card_two = 10
    else: card_two = int(card_two)
    
    total_value_in_hand = card_one + card_two

    if (total_value_in_hand + 11) > 21:
        return 1
    
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    if card_one in {"J", "K", "Q", "10"} and card_two == "A":
        return True
    
    if card_two in {"J", "K", "Q", "10"} and card_one == "A":
        return True
    
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_one in {"J", "K", "Q"} and card_two in {"J", "K", "Q"}:
        return True
    if card_one == card_two:
        return True
    
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if card_one == "A":
        card_one = 1
    if card_two == "A":
        card_two = 1

    if card_one in {"K", "Q", "J"}:
        card_one = 10
    else:
        card_one = int(card_one)

    if card_two in {"K", "Q", "J"}:
        card_two = 10
    else: card_two = int(card_two)
    
    total_value_in_hand = card_one + card_two

    if total_value_in_hand in {9, 10, 11}:
        return True
    
    return False


print(can_double_down("10", "2"))