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

    rounds = []

    while len(rounds) < 3:
        rounds.append(number)
        number += 1

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

    if number in rounds: return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    total = 0

    for num in hand:
        total += num

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

    total /= len(hand)

    average_of_first_and_last_number = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]

    if total in {average_of_first_and_last_number, median}:
        return True
    
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    odd_list= []
    even_list = []
    total_odd = 0
    total_even = 0
    control = 0


    for num in hand:
        if control % 2 == 0:
            odd_list.append(hand[control])
        else: 
            even_list.append(hand[control])

        control += 1

    for num in odd_list:
        total_odd += num 

    for num in even_list:
        total_even += num 

    total_odd /= len(odd_list)
    total_even /= len(even_list)

    if total_odd == total_even:
        return True
    
    return False
    

print(average_even_is_average_odd([1, 3, 5, 7, 9]))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11: hand[-1] = 11 * 2

    return hand