"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    rounds, iterator = [], 0

    while iterator != 3:
        rounds.append(number)
        number += 1
        iterator += 1

    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    if number in rounds:
        return True

    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    total = 0

    for digit in hand:
        total += digit

    return total / len(hand)

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    total = 0

    for num in hand:
        total += num

    actual_average = total / len(hand)

    average_of_first_and_second_number = (hand[0] + hand[-1]) / 2

    median = hand[len(hand) // 2]

    if actual_average in [average_of_first_and_second_number, median]:
        return True

    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    evens, odds, counter = [], [], 0

    for num in hand:
        if counter % 2 == 0:
            odds.append(num)
        else:
            evens.append(num)
        counter += 1

    return sum(odds) / len(odds) ==  sum(evens) / len(evens)

print(average_even_is_average_odd([12, 10, 2, 4, 6, 8, 10]))


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 11 * 2

    return hand