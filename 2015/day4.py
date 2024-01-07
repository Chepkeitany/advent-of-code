import hashlib

def compute_md5(value):
    """Comput the md5 hash of a given value"""
    # Convert the value to bytes, assuming the value is a string
    value_bytes = value.encode()

    # Create an MD5 hash object
    md5_obj = hashlib.md5()

    # Update the hash object with the bytes
    md5_obj.update(value_bytes)

    # Get the hexadecimal digest of the hash
    md5_hash = md5_obj.hexdigest()

    return md5_hash

def lowest_number(input, number_of_zeros, match):
    """Calculate the lowest number that can be appended to input to give md5 hash
    starting with at least 5 trailing zeros
    """
    # Brute force: try all the possible values from 1 to 100 million
    for i in range(1, 100000000):
        result = compute_md5(f'{input}{i}')
        if result[:number_of_zeros] == match:
            return i
    return -1

# Part 1
assert lowest_number('abcdef', 5, '00000')  == 609043,  "Failed on input abcdef"
assert lowest_number('pqrstuv', 5, '00000') == 1048970, "Failed on input pqrstuv"
assert lowest_number('yzbqklnj', 5, '00000') == 282749, "Failed on input yzbqklnj"

# Part 2

assert lowest_number('abcdef', 6, '000000')  == 6742839,  "Failed on input abcdef"
assert lowest_number('pqrstuv', 6, '000000') == 5714438, "Failed on input pqrstuv"
assert lowest_number('yzbqklnj', 6, '000000') == 9962624, "Failed on input yzbqklnj"

print("All tests passed")
