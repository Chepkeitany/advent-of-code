def double_previous_value(n):
    """
    Calculate the value by doubling the previous value starting from 1.
    For n, the value is 2^(n-1).
    """
    return 2 ** (n - 1)

# split by : and then by |
def find_total_winning_points(lines):
    total_winning_points = 0
    for line in lines:
        card, numbers = line.split(":")
        numbers = numbers.split("|")
        cards_you_have = numbers[0].split()
        winning_cards = numbers[1].split()
        numbers = [number for number in cards_you_have if number in winning_cards]
        # print(numbers)
        count = len(numbers)

        if (count == 0):
            continue
        elif (count == 1):
            points = 1
        if count > 1:
            points = double_previous_value(count)
        total_winning_points += points
    return total_winning_points


file = open("day4_all.txt", "r")
content = file.read()
file.close()
lines = content.split("\n")
print(find_total_winning_points(lines))
