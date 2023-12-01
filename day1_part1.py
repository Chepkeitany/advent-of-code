# Function to sum all the 2-digit numbers formed from first and last digit in each str
def sum_first_last_digits(strs):
    sum = 0
    for str in strs:
        # Find the first and last digit in the string
        first_digit = None
        last_digit = None
        for char in str:
            if char.isdigit():
                if first_digit is None:
                    first_digit = char
                last_digit = char
        sum += int(first_digit + last_digit)
    return sum

# Read input from file
file = open("day1_all.txt", "r")
content = file.read()
print(sum_first_last_digits(content.split("\n")))
file.close()
