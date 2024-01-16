'''
Part 1
Calculate the difference between the number of characters of code for string literals 
minus the number of characters in memory for the values of the strings in total 
for the entire file
Part 2
Encode each code representation as a new string and find the number of characters of 
the new encoded representation, including the surrounding double quotes
'''
def calculate_string_character_diff(lines):
    """Calculate the diff between count of character literals 
       and length of actual value of strings"""
    total = 0
    for line in lines:
        string_literals_count = len(list(line))

        char_count = len(eval(line))
        total += (string_literals_count - char_count)
        # evaluate string for actual characters

    return total

def calculate_encoded_string_diff(lines):
    """Calculate diff between new encoded string and original string"""
    total_diff = 0

    for line in lines:
        # Encoding the new string
        encoded_line = "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\""

        # Calculating the difference in length between the encoded and original string
        diff = len(encoded_line) - len(line)
        total_diff += diff

    return total_diff

with open("day8_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()
    # Part 1
    assert calculate_string_character_diff(content) == 1371, "Failed on main input - part1"

    # Part 2
    assert calculate_encoded_string_diff(content) == 2117, "Failed on main input - part2"
