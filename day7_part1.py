from collections import Counter

card_strength_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def calculate_total_winnings(card_hands_bid):
    """ Calculates the total winnings for a given list of card hands and bids. """
    total_winnings = 0
    # Create a dictionary of each card and its bid
    bid_by_hand = {}
    card_hands = []
    for card_hand_bid in card_hands_bid:
        card, bid = card_hand_bid.split(" ")
        bid_by_hand[card] = int(bid)
        card_hands.append(card)

    sorted_cards = sort_card_hands_by_strength(card_hands)    

    for i, card in enumerate(sorted_cards):
        bid = int(bid_by_hand[card])
        # print('Rank is ', i + 1, ' and bid is ', bid, 'card is ', card)
        total_winnings += bid * (i + 1)

    return total_winnings


def sort_card_hands_by_strength(hands):
    """ Sorts card hands based on their strength. """
    def sort_key(hand):
        hand_type_strength = evaluate_hand_strength(hand)
        sorted_based_on_card_strength = [card_strength_order[card] for card in hand]

        return (hand_type_strength, sorted_based_on_card_strength)

    return sorted(hands, key=sort_key, reverse=False)

def evaluate_hand_strength(cards):
    """ Returns the strength of a poker hand. """
    counts = Counter(cards)
    count_values = sorted(counts.values(), reverse=True)

    hand_rankings = {
        (5,): 7,
        (4, 1): 6,
        (3, 2): 5,
        (3, 1, 1): 4,
        (2, 2, 1): 3,
        (2, 1, 1, 1): 2,
        (1, 1, 1, 1, 1): 1
    }

    return hand_rankings[tuple(count_values)]


file = open("day7_all.txt", "r")
content = file.read()
card_hands_bid = content.split("\n")
print(calculate_total_winnings(card_hands_bid))
