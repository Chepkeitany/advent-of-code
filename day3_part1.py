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


def sum_part_numbers(lines):
    sum = 0
    for i, line in enumerate(lines):
        l = line.strip()
        n = 0
        is_part_number = False

        for position, character in enumerate(l):
            if character.isdigit():
                n = n*10 + int(character)
                # Check if the character is surrounded by a symbol
                # in a 3x3 grid centered on the character
                for gridRow in [-1, 0, 1]:
                    for gridCol in [-1, 0, 1]:
                        try:
                            cc = lines[i+gridRow][position+gridCol]
                            if cc != '.' and not cc.isdigit():
                                is_part_number = True
                        except IndexError:
                            continue
            if not character.isdigit() or position == len(l)-1:
                if is_part_number:
                    sum += n
                    # Reset the flag in order to test the next number
                    is_part_number = False
                n = 0
    return sum

file = open("day3_test.txt", "r")
content = file.read()
file.close()
lines = content.split("\n")

print("The sum of all part numbers is:")
print(sum_part_numbers(lines))
