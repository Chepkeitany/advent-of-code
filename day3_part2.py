### Test input matrix ###
import collections

[
    ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
    ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'], 
    ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'], 
    ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'], 
    ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']
]

def calculate_gear_ratio_sum(lines):
    total_gear_ratio_sum = 0
    gears = collections.defaultdict(list)

    for i, line in enumerate(lines):
        clean_line = line.strip()
        current_number = 0
        gear_position = None

        for pos, char in enumerate(clean_line):
            if char.isdigit():
                current_number = current_number * 10 + int(char)

                # Check surrounding characters in a 3x3 grid
                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        try:
                            surrounding_char = lines[i + row_offset][pos + col_offset]
                            if surrounding_char == '*' and not (row_offset == 0 and col_offset == 0):
                                gear_position = (i + row_offset, pos + col_offset)
                        except IndexError:
                            continue

            # Check if end of number or end of line
            if not char.isdigit() or pos == len(clean_line) - 1:
                if gear_position:
                    gears[gear_position].append(current_number)
                    if len(gears[gear_position]) == 2:
                        total_gear_ratio_sum += current_number * gears[gear_position][0]
                    gear_position = None
                current_number = 0

    return total_gear_ratio_sum

file = open("day3_all.txt", "r")
content = file.read()
file.close()
lines = content.split("\n")

print("The sum of all gear ratios is:")
print(calculate_gear_ratio_sum(lines))
