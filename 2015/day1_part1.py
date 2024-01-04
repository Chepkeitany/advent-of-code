def find_final_floor(input):
    final_floor = 0

    for char in input:
        if char == '(':
            final_floor += 1
        else:
            final_floor -= 1

    return final_floor

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

print("All tests passed!")