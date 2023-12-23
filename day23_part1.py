import sys
sys.setrecursionlimit(1000000)

slopes_directions = { '^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1) }
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find_longest_path(grid):
    rows, cols = len(grid), len(grid[0])

    starting_position = (0, 1)
    ending_position = (rows - 1, cols - 2)

    longest_path = [0]

    def is_within_grid(position, rows, cols):
        return 0 <= position[0] < rows and 0 <= position[1] < cols

    def dfs(current_position, path, visited):
        if current_position == ending_position:
            longest_path[0] = max(longest_path[0], len(path))
            return

        neighbors = directions

        if grid[current_position[0]][current_position[1]] in slopes_directions:
            neighbors = [slopes_directions[grid[current_position[0]][current_position[1]]]]


        for neighbor in neighbors:
            next_position = (current_position[0] + neighbor[0], current_position[1] + neighbor[1])
            if is_within_grid(next_position, rows, cols) and grid[next_position[0]][next_position[1]] != '#' and next_position not in visited:
                path.append(next_position)
                visited.add(next_position)
                dfs(next_position, path, visited)
                visited.remove(next_position)
                path.pop(-1)

    visited = set()
    dfs(starting_position, [], visited)

    return longest_path[0]

file = open("day23_all.txt", "r")
content = file.read()
input = content.split("\n")
lines = [list(line) for line in input if line.strip() != ""]
print(find_longest_path(lines))
