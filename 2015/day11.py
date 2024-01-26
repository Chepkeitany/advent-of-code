'''
Calculate new password based on requirements

Passwords must be exactly eight lowercase letters (for security reasons),
so he finds his new password by incrementing
Passwords must include one increasing straight of at least three letters,
like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken
for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters,
like aa, bb, or zz.
'''

ALLOWED_LETTERS = 'abcdefghjkmnpqrstuvwxyz'


def letter_to_index(letter):
    """Convert a letter to its index in ALLOWED_LETTERS."""
    return ALLOWED_LETTERS.index(letter)


def index_to_letter(index):
    """Convert an index to its corresponding letter in ALLOWED_LETTERS."""
    return ALLOWED_LETTERS[index]


def password_to_number(password):
    """Convert a password string to a number using base 23."""
    number = 0
    for letter in password:
        number = number * 23 + letter_to_index(letter)
    return number


def number_to_password(number):
    """Convert a number back to a password string using base 23."""
    password = ''
    for _ in range(8):
        index = number % 23
        password = index_to_letter(index) + password
        number //= 23
    return password


def increment_password(password):
    """Increment the password and return a new one."""
    number = password_to_number(password)
    # print(number)
    incremented_number = number + 1
    new_password = number_to_password(incremented_number)
    return new_password


def has_straight(password):
    """
    Check that passwords includes one increasing straight of at least three letters,
    like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    """
    for i in range(6):
        if ord(password[i]) == ord(password[i + 1]) - \
                1 == ord(password[i + 2]) - 2:
            return True
    return False


def has_doubles(password):
    """
    Check if password contains at least two different, non-overlapping pairs of letters,
    like aa, bb, or zz.
    """
    last_char = None
    count = 0
    doubles = set()

    for char in password:
        if char == last_char:
            count += 1
        else:
            if count >= 2:
                doubles.add(last_char)
            count = 1
            last_char = char

    if count >= 2:
        doubles.add(last_char)

    return len(doubles) >= 2


def get_new_password(old_password):
    """Generate new password based on the given rules"""
    while True:
        password = increment_password(old_password)
        if has_doubles(password) and has_straight(password):
            return password
        old_password = password

    return old_password


if __name__ == "__main__":
    assert get_new_password('abcdefgh') == "abcdffaa", "Failed on get_new_password('abcdefgh')"
    assert get_new_password('cqjxjnds') == "cqjxxyzz", "Failed on get_new_password('cqjxjnds')"
    assert get_new_password('cqjxxyzz') == "cqkaabcc", "Failed on get_new_password('cqjxxyzz')"

    print("All tests passed!")
