# # Here I will write my first instance of using dictionary
#
# # ab is a short for address book
# ab = {
#     'Maksym': 'bilmaksym@gmail.com',
#     'Natalya': 'ne_bill@gmail.com',
#     'Andrey': 'bil1977@gmail.com',
#     'Swaroop': 'swaroop@swaroopch.org'
# }
# print('Maksym\'s address is ', ab['Maksym'])
#
# # deleting a pair
# del ab['Andrey']
# print('\nThere are {} contacts in address book'.format(len(ab)))
#
# for name, address in ab.items():
#     print('Contact {0} at {1}'.format(name, address))
#
# # Adding a key-value pair
# ab['Guido'] = 'guido@python.org'
#
# if 'Guido' in ab:
#     print("\nGuido's address is", ab['Guido'])



def sum_of_hand(hand):
    sum_of_hand = 0
    num_of_aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            sum_of_hand += 10
        elif card in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            sum_of_hand += int(card)
        elif card == "A":
            num_of_aces += 1
    for i in range(num_of_aces):
        if sum_of_hand + 11 <= 21:
            sum_of_hand += 11
        elif sum_of_hand + 11 > 21:
            sum_of_hand += 1
    return sum_of_hand

print(sum_of_hand(['A', 'A', 'A', 'A']))

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """

    pass