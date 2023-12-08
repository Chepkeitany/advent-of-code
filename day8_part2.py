from itertools import cycle
from math import lcm
from functools import reduce

# Input
# Given the left/right instruction, find your way from the beginning destination to the end destination
# You could use a repeated R/L instruction to get to the destination

# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)

# Starting positions are all nodes ending with A
# In this example, it would be 11A and 22A
# We need to calculate the number of steps it takes for all ghosts to get to the destination at the same time
def calculate_steps_to_destination_node(lines, header):
    directions = {}
    ghost_starting_positions = []
    # Transform directions into a dictionary for easy lookup
    for line in lines:
        current_node, left_right_nodes = line.split(' = ')
        left_node, right_node = left_right_nodes[1:-1].split(', ')
        directions[current_node]= left_node, right_node

        if current_node.endswith('A'):
            ghost_starting_positions.append(current_node)

    print(ghost_starting_positions)
    ghost_steps = []
    for ghost_starting_position in ghost_starting_positions:
        steps = 0
        location = ghost_starting_position
        for direction in cycle(header):
            if direction == 'L':
                location = directions[location][0]
            elif direction == 'R':
                location = directions[location][1]
            else:
                raise ValueError()
            steps +=1
            if location.endswith('Z'):
                ghost_steps.append(steps)
                break

    # find the least common multiple of the ghost steps
    # If two ghosts take n and m steps to get to the destination, 
    # then the least common multiple of n and m is the number of steps it takes for both ghosts to get to the destination at the same time
    max_steps = reduce(lcm, ghost_steps, 1)

    return max_steps

with open("day8_all.txt") as file:
    header,_,*lines = file.read().splitlines()

steps = calculate_steps_to_destination_node(lines, header)
print(steps)
