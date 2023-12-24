from sympy import symbols, Eq, solve

def find_linear_path_intersection(start_A, rate_A, start_B, rate_B, X, Y):
    x = symbols('x')

    # Unpack the starting positions and rates of change
    x1_A, y1_A = start_A[0], start_A[1]
    dx_A, dy_A = rate_A[0], rate_A[1]
    x1_B, y1_B = start_B[0], start_B[1]
    dx_B, dy_B = rate_B[0], rate_B[1]

    # Calculate slopes and y-intercepts for both lines
    m_A = dy_A / dx_A
    c_A = y1_A - m_A * x1_A

    m_B = dy_B / dx_B
    c_B = y1_B - m_B * x1_B

    # Equations of the lines
    line_A = m_A * x + c_A
    line_B = m_B * x + c_B

    # Solve for the intersection
    intersection_x = solve(line_A - line_B, x)

    # Check if there's a valid intersection in the future
    if intersection_x:
        intersection_y = line_A.subs(x, intersection_x[0])
        intersection_x = intersection_x[0]
        t1 = (intersection_x - x1_A) / dx_A
        t2 = (intersection_x - x1_B) / dx_B
        if t1 < 0 or t2 < 0:
            return False
        if X <= intersection_x <= Y and X <= intersection_y <= Y:
            return True
        else:
            return False
    else:
        return False

def check_intersections_within_test_area(hailstones, X, Y):
    intersections = 0

    processed_hailstones = []
    for hailstone in hailstones:
        hailstone_parts = hailstone.split("@")
        coordinates = tuple(map(int, hailstone_parts[0].strip().split(",")))
        rates = tuple(map(int, hailstone_parts[1].strip().split(",")))
        processed_hailstones.append((coordinates, rates))

    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            haiilstone1 = processed_hailstones[i]
            hailstone2 = processed_hailstones[j]
            coordinates1, rates1 = haiilstone1
            coordinates2, rates2 = hailstone2
            if find_linear_path_intersection(coordinates1, rates1, coordinates2, rates2, X, Y):
                intersections += 1
    return intersections

file = open("day24_all.txt", "r")
content = file.read()
hailstones = content.split("\n")
# For test
# X, Y = (7, 27)
# For larger input
X, Y = (200000000000000, 400000000000000)
result = check_intersections_within_test_area(hailstones, X, Y)
print(result)
