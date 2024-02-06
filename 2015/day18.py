"""
Generate a lighting configuration using Conway's Game of Life
after n steps
"""


def count_neighbors(grid, x, y):
    """Count alive neighbors for the cell at (x, y)."""
    count = 0

    neighbors = [
        (i,j) for i in range(x - 1, x + 2)
              for j in range(y - 1, y + 2) if (i,j) != (x,y)
            ]
    count = 0
    for i, j in neighbors:
        if 0 <= i < len(grid) and 0 <= j < len(
                grid[0]) and grid[i][j] == '#':  # Assuming # is alive, . is dead
            count += 1
    return count


def game_of_life_step(grid):
    """Compute one step of Conway's Game of Life"""
    new_grid = [['.' for _ in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == '#' and neighbors in [2, 3]:
                new_grid[i][j] = '#'
            elif grid[i][j] == '.' and neighbors == 3:
                new_grid[i][j] = '#'

    return new_grid


def count_lights_on(grid):
    """Count the number of lights that are on"""
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                count += 1

    return count


if __name__ == "__main__":
    with open("day18_test.txt", encoding="utf-8") as f:
        grid = [list(line) for line in f.read().split("\n") if line.strip() != ""]

        for _ in range(4):
            grid = game_of_life_step(grid)

        assert count_lights_on(grid) == 4, "Failed on test input"

    with open("day18_all.txt", encoding="utf-8") as f:
        grid = [list(line) for line in f.read().split("\n") if line.strip() != ""]

        for _ in range(100):
            grid = game_of_life_step(grid)

        assert count_lights_on(grid) == 821, "Failed on main input - part 1"
