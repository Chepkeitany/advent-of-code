'''
Count the number of nice strings based on the properties below.
A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
- It contains at least one letter that appears twice in a row, like xx, abcdde (dd), 
  or aabbccdd (aa, bb, cc, or dd).
- It does not contain the strings ab, cd, pq, or xy,
  even if they are part of one of the other requirements.
'''
def has_double_letters(s):
    """Check if a string has at least one double letter"""
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False
def is_nice_string(s):
    """Check if a string matches the properties of a nice string"""
    # Check if it contains at least three vowels
    vowels = 'aeiou'
    vowel_count = sum(x in vowels for x in s)

    # Check if str contains at least one letter that appears twice in a row
    exists_double_letter = has_double_letters(s)

    # Check that the str does not contain the strings ab, cd, pq, or xy
    disallowed_strings = ["ab", "cd", "pq", "xy"]
    contains_disallowed_str = False
    for disallowed_string in disallowed_strings:
        if disallowed_string in s:
            contains_disallowed_str = True
            break

    return vowel_count >= 3 and exists_double_letter and (not contains_disallowed_str)

def count_nice_strings(lines):
    """Count the number of nice strings in the given input"""
    nice_strings_count = 0
    for line in lines:
        if is_nice_string(line):
            nice_strings_count += 1

    return nice_strings_count

# Test input
with open("day5_test.txt", encoding="utf-8") as file:
    test_content = file.read().splitlines()
    assert count_nice_strings(test_content) == 2, "Failed on test input"

# Main input
with open("day5_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()
    assert count_nice_strings(content) == 255, "Failed on main input"

print("All tests passed!")
