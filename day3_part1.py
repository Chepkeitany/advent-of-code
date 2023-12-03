### Test input matrix ###
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

def calculate_part_number_sum(lines):
    total_part_number_sum = 0

    for i, line in enumerate(lines):
        clean_line = line.strip()
        current_number = 0
        valid_part_number = False

        for pos, char in enumerate(clean_line):
            if char.isdigit():
                current_number = current_number * 10 + int(char)

                # Check surrounding characters in a 3x3 grid
                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        try:
                            surrounding_char = lines[i + row_offset][pos + col_offset]
                            if surrounding_char != '.' and not surrounding_char.isdigit():
                                valid_part_number = True
                        except IndexError:
                            continue

            # Check if end of number or end of line
            if not char.isdigit() or pos == len(clean_line) - 1:
                if valid_part_number:
                    total_part_number_sum += current_number
                    valid_part_number = False
                current_number = 0

    return total_part_number_sum

file = open("day3_test.txt", "r")
content = file.read()
file.close()
lines = content.split("\n")

print("The sum of all part numbers is:")
print(calculate_part_number_sum(lines))
