'''
To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible from the lava pool to the machine parts factory.
To do this, you need to minimize heat loss while choosing a route that doesn't require the crucible to go in a straight line for too long.

Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, 
and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.

For example:

2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533

Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block. 
The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block. 
(Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)

Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

One way to minimize heat loss is this path:

2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>

This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.

Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?
'''

# This is part 1
# The idea is to use BFS to find the shortest path from the top-left to the bottom-right that minimizes the heat loss.
# The heat loss is the sum of the numbers in the path.
# We need to keep track that the crucible can't move more than 3 consecutive blocks in the same direction.
# Also, the crucible can't reverse direction, after entering each city block, it may only turn left, continue straight, or turn right.
#

import heapq

# Function to add an item to the queue
def add_item(queue, item):
    heapq.heappush(queue, item)

# Function to pop an item from the queue
def pop_item(queue):
    smallest_item = heapq.heappop(queue)
    # Reorder the tuple to its original form before returning
    return (smallest_item[0], smallest_item[1], smallest_item[2], smallest_item[3])

def calculate_path_with_least_heat_loss(input):
    min_heat_loss = float("inf")
    ending_position = (len(input) - 1, len(input[0]) - 1)
    priority_queue = []

    maximum_streak = 3

    up, down, left, right = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # Add the starting positions to the queue
    # From top-left, the crucible can only move right or down
    # right
    add_item(priority_queue, (input[0][1], (0, 1), right, 1)) # (heat_loss, row, col, direction, streak_in_same_direction)
    # down
    add_item(priority_queue, (input[1][0], (1, 0), down, 1)) # (heat_loss, row, col, direction, streak_in_same_direction)

    def is_within_bounds(row, col):
        return 0 <= row < len(input) and 0 <= col < len(input[0])

    visited = set()
    while len(priority_queue) > 0:
        # Pop the item with the least heat loss
        heat_loss, (row, col), (direction_x, direction_y), streak = pop_item(priority_queue)

        if ((row, col), (direction_x, direction_y), streak) in visited:
            continue

        # add the current popped item to the visited set
        visited.add(((row, col), (direction_x, direction_y), streak))

        if (row, col) == ending_position and streak <= maximum_streak:
            min_heat_loss = min(min_heat_loss, heat_loss)
            return min_heat_loss

        if streak < maximum_streak:
            # Check if the crucible can move in the same direction
            # If it can, add the next position to the queue
            next_row = row + direction_x
            next_col = col + direction_y
            if is_within_bounds(next_row, next_col) and ((next_row, next_col), (direction_x, direction_y), streak + 1) not in visited:
                next_heat_loss = heat_loss + input[next_row][next_col]
                add_item(priority_queue, (next_heat_loss, (next_row, next_col), (direction_x, direction_y), streak + 1))

        # Move the crucible to the left or right
        # turn 90 degrees to the left
        left_direction_x, left_direction_y = (direction_y, -direction_x)
        left_position = (row + left_direction_x, col + left_direction_y)
        if is_within_bounds(left_position[0], left_position[1]) and ((left_position), (left_direction_x, left_direction_y), 1) not in visited:
            new_heat_loss = heat_loss + input[left_position[0]][left_position[1]]
            add_item(priority_queue, (new_heat_loss, (left_position[0], left_position[1]), (left_direction_x, left_direction_y), 1))

        # turn 90 degrees to the right
        right_direction_x, right_direction_y = (-direction_y, direction_x)
        right_position = (row + right_direction_x, col + right_direction_y)
        if is_within_bounds(right_position[0], right_position[1]) and ((right_position), (right_direction_x, right_direction_y), 1) not in visited:
            new_heat_loss = heat_loss + input[right_position[0]][right_position[1]]
            add_item(priority_queue, (new_heat_loss, (right_position[0], right_position[1]), (right_direction_x, right_direction_y), 1))

    return min_heat_loss

file = open("day17_all.txt", "r")
content = file.read()
content = [list(map(int, line)) for line in content.split("\n")]

print(calculate_path_with_least_heat_loss(content))
