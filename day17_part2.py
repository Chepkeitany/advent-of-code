'''
This is part2 
The crucibles of lava simply aren't large enough to provide an adequate supply of lava to the machine parts factory. 
Instead, the Elves are going to upgrade to ultra crucibles.

Ultra crucibles are even more difficult to steer than normal crucibles. 
Not only do they have trouble going in a straight line, but they also have trouble turning!

Once an ultra crucible starts moving in a direction, it needs to move a minimum of four blocks in that direction before it can turn (or even before it can stop at the end). However, it will eventually start to get wobbly: an ultra crucible can move a maximum of ten consecutive blocks without turning.
'''
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

    maximum_streak = 10

    minimum_stream = 4

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

        # Move the crucible to the left or right only if it has moved at least 4 blocks in the same direction
        if streak >= minimum_stream:
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
