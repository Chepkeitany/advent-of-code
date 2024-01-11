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

def turn_on_part2(grid, x_start, y_start, x_end, y_end):
    """Increase the brightness of the lights in the specified coordinates by 1"""
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            grid[i][j] += 1

def turn_off_part2(grid, x_start, y_start, x_end, y_end):
    """Decrease the brightness of lights in the specified coordinates. by 1, to a minimum of zero"""
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            grid[i][j] -= 1
            if grid[i][j] < 0:
                grid[i][j] = 0

def toggle_part2(grid, x_start, y_start, x_end, y_end):
    """Increase the brightness of the lights in the specified coordinates by 2"""
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            grid[i][j] += 2

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

def calculate_total_brightness_of_lights(lines):
    """Calculate total brightness after all the instructions"""
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        # split based on space
        instruction = line.split()
        if instruction[0] == 'turn':
            x_start, y_start = [int(i) for i in instruction[2].split(',')]
            x_end, y_end = [int(i) for i in instruction[4].split(',')]
            if instruction[1] == "on":
                turn_on_part2(grid, x_start, y_start, x_end, y_end)
            else:
                # turn off instruction
                turn_off_part2(grid, x_start, y_start, x_end, y_end)

        else:
            # this is a toggle instruction
            x_start, y_start = [int(i) for i in instruction[1].split(',')]
            x_end, y_end = [int(i) for i in instruction[3].split(',')]
            toggle_part2(grid, x_start, y_start, x_end, y_end)

    # Calculate total brightness
    total_brightness = 0
    for row in grid:
        for value in row:
            total_brightness += value

    return total_brightness
with open('day6_all.txt', encoding="utf-8") as file:
    content = file.read().splitlines()
    # Part 1 - Main input
    print(count_number_of_lit_lights(content))
    assert count_number_of_lit_lights(content) == 543903, "Failed on main input - part1"
    # Part 2 - Main input
    # print(calculate_total_brightness_of_lights(content))
    assert calculate_total_brightness_of_lights(content) == 14687245, "Failed on main input - part2"
    print("All tests passed!")
