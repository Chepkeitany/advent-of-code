from collections import deque

# Directions: north, south, west, east
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def calculate_garden_plots_reached(lines):
    # Identify the starting position, marked by S
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "S":
                start = (row, col)
                break

    row, col = start
    queue = deque([(start)]) # Starting position is S

    visited_garden_plots = set()
    for i in range(64):
        # Reset the visited garden plots and the queue for the next iteration
        new_queue = deque()
        visited_garden_plots = set()
        
        while queue:
            row, col = queue.popleft()

            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                new_position = (new_row, new_col)

                if new_row < 0 or new_row >= len(lines) or new_col < 0 or new_col >= len(lines[0]):
                    continue

                # valid position
                if lines[new_row][new_col] != "#":
                    # and not visited
                    if new_position not in visited_garden_plots:
                        visited_garden_plots.add(new_position)
                        new_queue.append((new_position))

        # print("Number of visited garden plots after {} steps is {} ".format(i + 1, len(visited_garden_plots)))
        # Update the queue for the next iteration
        queue = new_queue
    return len(visited_garden_plots)

file = open("day21_all.txt", "r")
content = file.read()
content = content.split("\n")
lines = [list(line) for line in content]
result = calculate_garden_plots_reached(lines)
print(result)
