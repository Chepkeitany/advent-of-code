from collections import deque

def calculate_number_of_energized_tiles(input, start=(0, 0), start_direction="right"):
    rows, cols = (len(input), len(input[0]))
    UP, DOWN, LEFT, RIGHT = "up", "down", "left", "right"
    directions = {
        RIGHT: (0, 1),
        DOWN:  (1, 0),
        LEFT:  (0, -1), 
        UP: (-1, 0)
    }

    # Do a BFS
    queue = deque([(start, start_direction)]) # position, direction
    visited = set()

    energized_cells = set()

    def validate_and_add_to_queue(row, col, direction):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if ((row, col), direction) not in visited:
            queue.append(((row, col), direction))
            visited.add(((row, col), direction))
            energized_cells.add((row, col))

    energized_cells.add(start)
    visited.add((start, RIGHT))
    while queue:
        position, direction = queue.popleft()
        row, col = position

        if row < 0 or row >= rows or col < 0 or col >= cols:
            continue

        if input[row][col] == '.': # empty space
            row_delta, col_delta = directions[direction]
            new_row = row + row_delta
            new_col = col + col_delta
            if ((new_row, new_col), direction) not in visited:
                queue.append(((new_row, new_col), direction))
            validate_and_add_to_queue(new_row, new_col, direction)
        elif input[row][col] == "-": # splitter
            if direction == "up" or direction == "down":
                left_row = row + directions["left"][0]
                left_col = col + directions["left"][1]
                right_row = row + directions["right"][0]
                right_col = col + directions["right"][1]

                validate_and_add_to_queue(left_row, left_col, LEFT)
                validate_and_add_to_queue(right_row, right_col, RIGHT)
            else:
                row_delta, col_delta = directions[direction]
                row += row_delta
                col += col_delta

                validate_and_add_to_queue(row, col, direction)
        if input[row][col] == "/": # mirror
            if direction == "right":
                direction = "up"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "down"
            elif direction == "up":
                direction = "right"
            row_delta, col_delta = directions[direction]
            row += row_delta
            col += col_delta

            validate_and_add_to_queue(row, col, direction)
        elif input[row][col] == "\\": # mirror
            if direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "right"
            elif direction == "left":
                direction = "up"
            elif direction == "up":
                direction = "left"
            row_delta, col_delta = directions[direction]
            row += row_delta
            col += col_delta

            validate_and_add_to_queue(row, col, direction)
        elif input[row][col] == "|": # splitter
            if direction == "right" or direction == "left":
                up_row = row + directions["up"][0]
                up_col = col + directions["up"][1]
                down_row = row + directions["down"][0]
                down_col = col + directions["down"][1]
                validate_and_add_to_queue(up_row, up_col, UP)
                validate_and_add_to_queue(down_row, down_col, DOWN)
            else:
                row_delta, col_delta = directions[direction]
                row += row_delta
                col += col_delta
                validate_and_add_to_queue(row, col, direction)

    return len(energized_cells)

file = open("day16_all.txt", "r")
content = file.read()
content = [list(line) for line in content.split("\n")]

# This is part 1
# print(calculate_number_of_energized_tiles(content, (0, 0), "right"))

# Part 2
# the beam enters from any edge tile and heading away from that edge. 
# (You can choose either of two directions for the beam if it starts on a corner; 
# for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

# So, the beam could start on any tile in the top row (heading downward), 
# any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), 
# or any tile in the rightmost column (heading left). 
# To produce lava, you need to find the configuration that energizes as many tiles as possible.

# Let's try all 4 corners
top_left, top_right, bottom_left, bottom_right = [(0, 0), (0, len(content[0]) - 1), (len(content) - 1, 0), (len(content) - 1, len(content[0]) - 1)]
max_energized_tiles = -1

# From top-left corner, the beam can down or right
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, top_left, "down"))
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, top_left, "right"))

# From top-right corner, the beam can down or left
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, top_right, "down"))
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, top_right, "left"))

# From bottom-left corner, the beam can up or right
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, bottom_left, "up"))
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, bottom_left, "right"))

# From bottom-right corner, the beam can up or left
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, bottom_right, "up"))
max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, bottom_right, "left"))


# Now, let's try each tile on the top row (excluding the corners)
for col in range(1, len(content[0]) - 1):
    max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, (0, col), "down"))

# Then we try each tile on the bottom row (excluding the corners)
for col in range(1, len(content[0]) - 1):
    max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, (len(content) - 1, col), "up"))

# Then we try each tile on the leftmost column (excluding the corners)
for row in range(1, len(content) - 1):
    max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, (row, 0), "right"))

# Then we try each tile on the rightmost column (excluding the corners)
for row in range(1, len(content) - 1):
    max_energized_tiles = max(max_energized_tiles, calculate_number_of_energized_tiles(content, (row, len(content[0]) - 1), "left"))

print(max_energized_tiles)



