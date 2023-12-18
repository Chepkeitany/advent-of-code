'''
Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a large supply of lava for a while; the Elves have already started creating a large lagoon nearby for this purpose.

However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.

When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######
At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######
Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?
'''

dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

def calculate_lava_area(input):
    x = y = perimeter = 0
    # vertices represents the coordinates of the borders of the polygon
    vertices = []
    for row in input:
        direction, distance_meters, hex_code = row.split()
        distance_meters = int(distance_meters)
        # print(direction, distance_meters, hex_code)

        (direction_x, direction_y), m = directions[direction], distance_meters
        vertices.append((x, y))
        perimeter += distance_meters

        x += direction_x * distance_meters
        y += direction_y * distance_meters

    # Calculate the area of the polygon formed by the borders since the coordinates of its vertices are known using the Shoelace Formula
    n = len(vertices)

    area = 0
    sum1 = sum2 = 0
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n] # This ensures the last vertex connects to the first
        sum1 += x1 * y2
        sum2 += y1 * x2

    area = abs(sum1 - sum2) / 2

    # We need to calculate the interior area, which it the number of points inside the polygon
    # From Shoelace formula, we found the area of the polygon, A
    # Pick's Theorem says that A = i + b / 2 - 1, where A is the area of the polygon, i is the number of internal integer points, and b is the number of boundary integer points.
    # b is the perimeter, which we already have
    # We want the internal points, so we have some algebra to do.

    # A = i + perimeter / 2 - 1
    # i = A - perimeter / 2 + 1

    interior_area = area - perimeter // 2 + 1

    # Total lava area is the interior area plus the perimeter
    return interior_area + perimeter


file = open("day18_all.txt", "r")
content = file.read()
content = content.split("\n")
result = calculate_lava_area(content)
print(result)
