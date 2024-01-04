def find_final_floor(input):
    final_floor = 0

    for char in input:
        if char == '(':
            final_floor += 1
        else:
            final_floor -= 1

    return final_floor

def find_basement_position(input):
    final_floor = 0

    for index, char in enumerate(input):
        if char == '(':
            final_floor += 1
        else:
            final_floor -= 1
        if final_floor == -1:
            return index + 1

    return final_floor

# Part 1
# Sample test cases
assert find_final_floor('(())') == 0,     "Failed on input (())"
assert find_final_floor('()()') == 0,     "Failed on input ()()"
assert find_final_floor('(((') == 3,      "Failed on input ((("
assert find_final_floor('(()(()(') == 3,  "Failed on input (()(()("
assert find_final_floor('))(((((') == 3,  "Failed on input ))((((("
assert find_final_floor('())') == -1,     "Failed on input ())"
assert find_final_floor(')())())') == -3, "Failed on input )())())"

# Main input
file = open("day1_input.txt", "r")
input = file.read()
result = find_final_floor(input)
assert result == 280, "Failed on puzzle input!"


# Part 2
# Sample test case
assert find_basement_position('()())') == 5, "Failed on input ()())"

# Main input
assert find_basement_position(input) == 1797, "Failed on puzzle input"

print("All tests passed!")
