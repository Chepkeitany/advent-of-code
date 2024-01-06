directions_map = {
        '^': (-1,0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
}
def find_houses_visited(input):
    # Assume starting, position is (0,0)
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

def find_houses_visited_with_turns(input):
    # Assume both santa and robo-santa start at position (0,0)
    santas_location = (0, 0)
    robo_santas_location = (0, 0)
    visited_houses_coords = set()
    visited_houses_coords.add(santas_location)
    santas_turn = True
    robo_santas_turn = False

    for direction in input:
        new_direction_coord = directions_map[direction]
        if santas_turn:
            new_house_location = (santas_location[0] + new_direction_coord[0],
                                santas_location[1] + new_direction_coord[1])
            santas_location = new_house_location
            visited_houses_coords.add(new_house_location)
            santas_turn = False
            robo_santas_turn = True
        else:
            new_house_location = (robo_santas_location[0] + new_direction_coord[0],
                                robo_santas_location[1] + new_direction_coord[1])
            robo_santas_location = new_house_location
            visited_houses_coords.add(new_house_location)
            robo_santas_turn = False
            santas_turn = True

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

# Part 2
# Sample test cases
assert find_houses_visited_with_turns('^v') == 3,         "Failed on input ^v"
assert find_houses_visited_with_turns('^v^v^v^v^v') == 11, "Failed on input ^v^v^v^v^v"
assert find_houses_visited_with_turns('^>v<') == 3,          "Failed on input >"
assert find_houses_visited_with_turns('<') == 2,          "Failed on input <"

# Main input
file = open("day3_all.txt", "r")
input = file.read()
result = find_houses_visited_with_turns(input)
assert result == 2631, "Failed on puzzle input!"

print("All tests passed!")