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

def lowest_number(input, number_of_zeros):
    """Calculate the lowest number that can be appended to input to give md5 hash
    starting with at least 5 trailing zeros
    """
    # Brute force: try all the possible values from 1 to 100 million
    for i in range(1, 100000000):
        result = compute_md5(f'{input}{i}')
        if result[:number_of_zeros] == '00000':
            return i
    return -1

# Part 1
assert lowest_number('abcdef', 5)  == 609043,  "Failed on input abcdef"
assert lowest_number('pqrstuv', 5) == 1048970, "Failed on input pqrstuv"
assert lowest_number('yzbqklnj', 5) == 282749, "Failed on input yzbqklnj"

print("All tests passed!")

