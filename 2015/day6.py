'''
Count the number of lights lit in the grid
'''

def turn_on(grid, x_start, y_start, x_end, y_end):
    """Turn on lights in the specified coordinates."""
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            grid[i][j] = 1

def turn_off(grid, x_start, y_start, x_end, y_end):
    """Turn off lights in the specified coordinates."""
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            grid[i][j] = 0

def toggle(grid, x_start, y_start, x_end, y_end):
    """Toggle lights in the specified coordinates."""
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            grid[i][j] = 1 - grid[i][j]

def count_number_of_lit_lights(lines):
    """Count how many lights are lit after all the instructions"""
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        # split based on space
        instruction = line.split()
        if instruction[0] == 'turn':
            x_start, y_start = [int(i) for i in instruction[2].split(',')]
            x_end, y_end = [int(i) for i in instruction[4].split(',')]
            if instruction[1] == "on":
                turn_on(grid, x_start, y_start, x_end, y_end)
            else:
                # turn off instruction
                turn_off(grid, x_start, y_start, x_end, y_end)

        else:
            # this is a toggle instruction
            x_start, y_start = [int(i) for i in instruction[1].split(',')]
            x_end, y_end = [int(i) for i in instruction[3].split(',')]
            toggle(grid, x_start, y_start, x_end, y_end)

    # Count of the lights that are on
    lights_on_count = 0
    for row in grid:
        for value in row:
            if value == 1:
                lights_on_count += 1

    return lights_on_count

with open('day6_all.txt', encoding="utf-8") as file:
    content = file.read().splitlines()
    # print(count_number_of_lit_lights(content))
    # Part 1 - Main input
    assert count_number_of_lit_lights(content) == 543903, "Failed on main input"
