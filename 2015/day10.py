'''
Look and say.
For example 111221 is three 1s, two 2s, and one 1.
It becomes 312211
'''
def look_and_say(digits):
    '''Look and say the digits to form a new string'''
    result = []

    current = digits[0]
    idx = 0
    while idx < len(digits):
        count = 0
        new_idx = idx
        while new_idx < len(digits) and digits[new_idx] == current:
            count += 1
            new_idx += 1
        result.append(str(count))
        result.append(current)

        # print(new_idx)
        if new_idx < len(digits):
            idx = new_idx
            current = digits[new_idx]
        else:
            break

    return result

if __name__ == "__main__":
    # Test input
    current_input = '1'
    for i in range(5):
        result = ''.join(look_and_say(current_input))
        current_input = result

    assert current_input == '312211', "Failed on test input"

    # Main input
    current_input = '3113322113'
    for i in range(50):
        result = ''.join(look_and_say(current_input))
        if i == 39:
            # Part 1
            assert len(result) == 329356, "Failed on main input - part 1"
        current_input = result

    # Part 2
    assert len(current_input) == 4666278, "Failed on main input - part 2"

    print("All tests passed!")
