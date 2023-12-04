cards_dictionary = {}

def find_total_scratchcards(lines):
    total_scratchcards = 0
    for line in lines:
        card, numbers = line.split(":")
        card_number = int(card.split()[1])
        numbers = numbers.split("|")
        cards_you_have = numbers[0].split()
        winning_cards = numbers[1].split()
        numbers = [number for number in cards_you_have if number in winning_cards]
        # print(numbers)
        count = len(numbers)
 
        cards_dictionary[card_number] = cards_dictionary.get(card_number, 0) + 1
        starting_card = card_number + 1
        count_previous_cards = cards_dictionary.get(card_number, 0)

        i = 1
        while (i < count + 1):
            for j in range(0, count_previous_cards):
                cards_dictionary[starting_card] = cards_dictionary.get(starting_card, 0) + 1
            starting_card = starting_card + 1
            i += 1

        card_copies = cards_dictionary[card_number]

        total_scratchcards += card_copies
    # for card in cards_dictionary:
    #     print(card, cards_dictionary[card])
    return total_scratchcards


file = open("day4_all.txt", "r")
content = file.read()
file.close()
lines = content.split("\n")
print(find_total_scratchcards(lines))
