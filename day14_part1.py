def calculate_total_load_on_north_beam(input):
    total_load = 0

    # Starting from the second row, we need to find the new positions for the rounded rocks
    # The rounded rocks will move to the furthest empty space up north possible
    # If it is blocked by a cube-shaped rock, it will stop there

    # We need to find the new positions for the rounded rocks
    for i in range(1, len(input)):
        row = input[i]
        for j in range(len(row)):
            if row[j] == "O":
                # If it is blocked by a cube-shaped rock, it will stop there
                # If it is blocked by another rounded rock, it will stop there
                # If it is blocked by the north edge of the platform, it will stop there
                # print("Found a rounded rock at row " + str(i) + " and column " + str(j))
                # Find the furthest empty space up north possible on the same column
                new_row_position = i
                starting_row = i - 1
                while starting_row >= 0:
                    if input[starting_row][j] == ".":
                        new_row_position = starting_row
                    else:
                        break
                    starting_row -= 1

                if (new_row_position == i):
                    # print("No empty space found for rounded rock at row " + str(i) + " and column " + str(j))
                    continue
                else:
                    # Move the rounded rock to the new position
                    input[new_row_position][j] = "O"

                    # Reset the old position to empty space
                    input[i][j] = "."

                    # print("New row position for rounded rock at row " + str(i) + " and column " + str(j) + " is " + str(new_row_position))


    # Calculate the load
    # Go through each row and find the total number of rounded rocks in that row
    # Multiply that number by the row number and add to the total load
    # The topmost row is actually identified as len(rows) + 1
    rows = len(input)
    for i in range(len(input)):
        row = input[i]
        number_of_rounded_rocks = 0
        for j in range(len(row)):
            if row[j] == "O":
                number_of_rounded_rocks += 1

        # print(number_of_rounded_rocks, (rows - i))
        total_load += number_of_rounded_rocks * (rows - i)


    # print(total_load)

    return total_load

file = open("day14_all.txt", "r")
content = file.read()
input = content.split("\n")
lines = [list(line) for line in input if line.strip() != ""]
print(calculate_total_load_on_north_beam(lines))
