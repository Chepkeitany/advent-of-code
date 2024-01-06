def find_houses_visited(input):
    # Assume starting, position is (0,0)
    # When he visits north, coordinates change by (-1,0)
    # When he visits south, coordinates change by (1,0)
    # When he visits east, coordinates change by (0,1)
    # When he visits west, coordinates change by (0,-1)

    directions_map = {
        '^': (-1,0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }

    current_location = (0, 0)
    visited_houses_coords = set()
    visited_houses_coords.add(current_location)

    for direction in input:
        new_direction_coord = directions_map[direction]
        new_house_location = (current_location[0] + new_direction_coord[0],
                              current_location[1] + new_direction_coord[1])
        current_location = new_house_location
        visited_houses_coords.add(new_house_location)

    return len(visited_houses_coords)

# Part 1
# Sample test cases
assert find_houses_visited('^>v<') == 4,       "Failed on input ^>v<"
assert find_houses_visited('^v^v^v^v^v') == 2, "Failed on input ^v^v^v^v^v"
assert find_houses_visited('>') == 2,          "Failed on input >"
assert find_houses_visited('<') == 2,          "Failed on input <"
assert find_houses_visited('>>') == 3,         "Failed on input >>"

# Main input
file = open("day3_all.txt", "r")
input = file.read()
result = find_houses_visited(input)
assert result == 2572, "Failed on puzzle input!"
