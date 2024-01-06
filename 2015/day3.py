'''
Move santa and robo santa through an inifinite grid
'''
directions_map = {
        '^': (-1,0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
}
def find_houses_visited(input):
    '''Move santa through the grid based on directions in input'''
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
    '''Move santa and robo-santa in turns through the grid based on directions based on input'''
    # Assume both santa and robo-santa start at position (0,0)
    santas_location = (0, 0)
    robo_santas_location = (0, 0)
    visited_houses_coords = set()
    visited_houses_coords.add(santas_location)
    santas_turn = True

    for direction in input:
        new_direction_coord = directions_map[direction]
        if santas_turn:
            new_house_location = (santas_location[0] + new_direction_coord[0],
                                santas_location[1] + new_direction_coord[1])
            santas_location = new_house_location
            visited_houses_coords.add(new_house_location)
            santas_turn = False
        else:
            new_house_location = (robo_santas_location[0] + new_direction_coord[0],
                                robo_santas_location[1] + new_direction_coord[1])
            robo_santas_location = new_house_location
            visited_houses_coords.add(new_house_location)
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
with open("day3_all.txt", encoding="utf-8") as file:
    assert find_houses_visited(file.read()) == 2572, "Failed on puzzle input!"

# Part 2
# Sample test cases
assert find_houses_visited_with_turns('^v') == 3,         "Failed on input ^v"
assert find_houses_visited_with_turns('^v^v^v^v^v') == 11, "Failed on input ^v^v^v^v^v"
assert find_houses_visited_with_turns('^>v<') == 3,          "Failed on input >"
assert find_houses_visited_with_turns('<') == 2,          "Failed on input <"

# Main input
with open("day3_all.txt", encoding="utf-8") as file:
    assert find_houses_visited_with_turns(file.read()) == 2631, "Failed on puzzle input!"

print("All tests passed!")
