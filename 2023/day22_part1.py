from collections import defaultdict

def is_at_bottom(brick):
    # the lowest z value a brick can have is 1,
    # so if the z value of the first point of the brick is 1, then the brick is at the bottom
    return brick[0][2] == 1

def is_blocked(brick, grid):
    # Calculate the range of x, y, and z coordinates covered by the brick
    x_range = range(brick[0][0], brick[1][0] + 1)
    y_range = range(brick[0][1], brick[1][1] + 1)
    z_below = brick[0][2] - 1  # The z level just below the brick

    # Check each point below the brick
    for x in x_range:
        for y in y_range:
            if (x, y, z_below) in grid:
                return True  # Return True if any point below is blocked

    # If no point below is blocked, return False
    return False

def is_brick_safe_to_remove(bricks, i):
    new_bricks = bricks[:i] + bricks[i + 1 :] # Create a copy of the bricks list with the ith brick removed
    return new_bricks == drop_bricks_to_bottom(new_bricks)[0]

def move_brick_down(brick):
    # Subtract 1 from the z coordinate of each point in the brick
    return (
        (brick[0][0], brick[0][1], brick[0][2] - 1),
        (brick[1][0], brick[1][1], brick[1][2] - 1)
    )

def update_grid(brick, grid):
    for z in range(brick[0][2], brick[1][2] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            for x in range(brick[0][0], brick[1][0] + 1):
                grid.add((x, y, z))

def drop_bricks_to_bottom(bricks):
    bricks_final_positions = []
    grid = set()
    fall_count = 0

    for brick in bricks:
        # Initialize fall distance
        fall_distance = 0

        # Determine the fall distance
        while not is_at_bottom(brick) and not is_blocked(brick, grid):
            brick = move_brick_down(brick)
            fall_distance += 1

        # Update new position of the brick
        bricks_final_positions.append(brick)
        update_grid(brick, grid)

        # Increment fall count if the brick has fallen
        if fall_distance:
            fall_count += 1

    return bricks_final_positions, fall_count
def calculate_disintegrated_bricks(input):
    # for line in input.splitlines():
    #     brick_ends_coords = [x.split(",") for x in line.split('~')]
    #     brick_ends_coords = [[int(x) for x in y] for y in brick_ends_coords]

    # Get the brick coordinates, a line like  2,2,2~2,2,2 means that both ends of the brick are at the same coordinate - in other words, that the brick is a single cube.
    # A line like 0,0,10~1,0,10 or 0,0,10~0,1,10 both represent bricks that are two cubes in volume, both oriented horizontally. 
    # The first brick extends in the x direction, while the second brick extends in the y direction.

    # We need to somehow stack the bricks on top of each other, so we need to know the orientation of the bricks
    # Then we can check if the brick is supported by another brick, if not, it can be disintegrated
    # We can use a dictionary to store the bricks, the key will be the brick number, the value will be a list of the coordinates of the brick
    # We can use a list to store the bricks that are supported by another brick
    # We can use a list to store the bricks that are not supported by another brick
    # Let's attempt some code now
    bricks = []

    for line in input.splitlines():
        brick_ends_coords = [x.split(",") for x in line.split('~')]
        brick_ends_coords = [[int(x) for x in y] for y in brick_ends_coords]
        bricks.append((brick_ends_coords[0], brick_ends_coords[1]))

    # Sort the bricks by the z coordinate of the first end of the brick
    bricks.sort(key=lambda x: x[0][2])

    # print(bricks)

    # Drop the bricks to the lowest position possible
    bricks_final_positions, fall_count = drop_bricks_to_bottom(bricks)
    # print(bricks_final_positions)

    bricks_can_be_disintegrated_count = 0
    for i in range(len(bricks_final_positions)):
        # Check if removing the brick does not affect the positions of other bricks
        if is_brick_safe_to_remove(bricks_final_positions, i):
            bricks_can_be_disintegrated_count += 1

    return bricks_can_be_disintegrated_count


file = open("day22_all.txt", "r")
content = file.read()
print(calculate_disintegrated_bricks(content))
