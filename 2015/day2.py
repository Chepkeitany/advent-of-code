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

        total_square_feet += smallest_side
        total_square_feet += 2 * l_w
        total_square_feet += 2 * w_h
        total_square_feet += 2 * h_l

    return total_square_feet

file = open("day2_all.txt")
content = file.read().splitlines()
print(calculate_total_square_feet(content))


