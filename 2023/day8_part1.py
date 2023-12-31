from itertools import cycle

# Input
# Given the left/right instruction, find your way from the beginning destination to the end destination
# You could use a repeated R/L instruction to get to the destination

## Example input

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)

# For instance starting at AAA, go right of AAA to CCC,
# Then at CCC, go left to ZZZ
# This takes 2 steps
def calculate_steps_to_destination_node(lines, header):
    directions = {}
    # Transform directions into a dictionary for easy lookup
    for line in lines:
        current_node, left_right_nodes = line.split(' = ')
        left_node, right_node = left_right_nodes[1:-1].split(', ')
        directions[current_node]= left_node, right_node

    steps = 0
    location = 'AAA'
    for direction in cycle(header):
        if direction == 'L':
            location = directions[location][0]
        elif direction == 'R':
            location = directions[location][1]
        else:
            raise ValueError()
        steps +=1
        if location == 'ZZZ':
            break

    return steps

with open("day8_all.txt") as file:
    header,_,*lines = file.read().splitlines()

steps = calculate_steps_to_destination_node(lines, header)
print(steps)
