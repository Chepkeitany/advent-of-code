extended_ascii_dict = {chr(i): i for i in range(256)}

def sum_hashed_values(input):
    # print (input)

    total_sum = 0

    for string in input:
        sum = 0
        for char in string:
            sum += extended_ascii_dict[char]
            sum *= 17
            sum %= 256
        total_sum += sum
    return total_sum

file = open("day15_all.txt", "r")
content = file.read()
content = content.split(",")

print(sum_hashed_values(content))
