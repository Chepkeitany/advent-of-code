'''
Check which line matches the detected items
'''
detected_items = {
    "children:": 3,
    "cats:": 7,
    "samoyeds:": 2,
    "pomeranians:": 3,
    "akitas:": 0,
    "vizslas:": 0,
    "goldfish:": 5,
    "trees:": 3,
    "cars:": 2,
    "perfumes:": 1
}


def check_part1(types, value):
    """Check which values match the detected_values exactly"""
    value = int(value)
    return detected_items[types] == value


def check_part2(types, value):
    """
    Check which values match the part 2 instructions:
    cats and trees readings indicates that there are greater than that many
    pomeranians and goldfish readings indicate that there are fewer than that many
    """
    value = int(value)
    if types in ("cats:", "trees:"):
        return detected_items[types] < value
    if types in ("pomeranians:", "goldfish:"):
        return detected_items[types] > value
    return detected_items[types] == value


if __name__ == "__main__":
    with open("day16.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split()

            # Part 1
            if (check_part1(line[2], line[3].strip(",")) and check_part1(
                    line[4], line[5].strip(",")) and check_part1(line[6], line[7])):
                print(line[1][:-1])
            # Part 2
            if (check_part2(line[2], line[3].strip(",")) and check_part2(
                    line[4], line[5].strip(",")) and check_part2(line[6], line[7])):
                print(int(line[1][:-1]))
