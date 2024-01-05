def calculate_total_square_feet(input):
    total_square_feet = 0
    for line in input:
        # Extract l, w, h
        lwh = line.split('x')
        l,w,h = [int(i) for i in lwh]
        l_w = l * w
        w_h = w * h
        h_l = h * l

        smallest_side = min(l_w, w_h, h_l)

        total_square_feet += 2 * l_w
        total_square_feet += 2 * w_h
        total_square_feet += 2 * h_l
        total_square_feet += smallest_side

    return total_square_feet

def calculate_smallest_perimeter(input):
    ribbon_length = 0
    for line in input:
        # Extract l, w, h
        lwh = line.split('x')
        l,w,h = [int(i) for i in lwh]
        l_w = l + w
        w_h = w + h
        h_l = h + l

        smallest_side = min(l_w, w_h, h_l)

        ribbon_length += 2 * smallest_side
        ribbon_length += l * w * h
    return ribbon_length

# Part 1
# Sample test cases
file = open("day2_test.txt")
content = file.read().splitlines()

assert calculate_total_square_feet(content) == 101,     "Failed on sample input"

file = open("day2_all.txt")
content = file.read().splitlines()
assert calculate_total_square_feet(content) == 1598415, "Failed on main input"

# Part 2
# Sample test cases
file = open("day2_test.txt")
content = file.read().splitlines()

assert calculate_smallest_perimeter(content) == 48,     "Failed on sample input"

file = open("day2_all.txt")
content = file.read().splitlines()
assert calculate_smallest_perimeter(content) == 3812909, "Failed on main input"

print("All tests passed!")
