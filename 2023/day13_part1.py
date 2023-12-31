def is_horizontal_reflection(rows, pattern):
    reflection_row = -1
    for i in range(0, rows - 1):
        first_row = pattern[i]
        second_row = pattern[i + 1]

        row_match = True
        for j in range(len(pattern[0])):
            if first_row[j] != second_row[j]:
                row_match = False
                break

        if row_match and validate_horizontal_reflection_point(pattern, i):
            return i

    return reflection_row

def validate_horizontal_reflection_point(pattern, i):
    rows = len(pattern)

    start = i
    end = i + 1

    while start >= 0 and end < rows:
        row_match = True
        first_row = pattern[start]
        second_row = pattern[end]
        for j in range(len(pattern[0])):
            if first_row[j] != second_row[j]:
                row_match = False
                break
        if not row_match:
            return False
        else:
            start -= 1
            end += 1

    return True

def is_vertical_reflection(cols, pattern):
    reflection_col = -1
    for i in range(0, cols - 1):
        first_col = i
        second_col = i + 1

        col_match = True
        for j in range(len(pattern)):
            if pattern[j][first_col] != pattern[j][second_col]:
                col_match = False
                break

        if col_match and validate_vertical_reflection_point(pattern, i):
            return i

    return reflection_col

def validate_vertical_reflection_point(pattern, i):
    cols = len(pattern[0])

    start = i
    end = i + 1

    while start >= 0 and end < cols:
        col_match = True
        for j in range(len(pattern)):
            if pattern[j][start] != pattern[j][end]:
                col_match = False
                break
        if not col_match:
            return False
        else:
            start -= 1
            end += 1

    return True


def sum_reflection_details(patterns):
    sum = 0
    for pattern in patterns:
        rows, cols = len(pattern), len(pattern[0])
        
        # Find out if reflection is on horizontal line
        reflection_on_row = is_horizontal_reflection(rows, pattern)

        if reflection_on_row != -1:
            number_of_rows_to_left = reflection_on_row + 1
            sum += (number_of_rows_to_left * 100)
        else:
            reflection_on_col = is_vertical_reflection(cols, pattern)
            number_of_columns_to_the_left = reflection_on_col + 1

            sum += number_of_columns_to_the_left
    return sum

patterns = []
pattern = []

with open("day13_all.txt") as file:
    for line in file:
        if line == "\n":
            patterns.append(pattern)
            pattern = []
        else:
            content = line.split("\n")
            pattern.append(list(content[0]))

    if pattern:
        patterns.append(pattern)

# for pattern in patterns:
#     print(pattern)
print(sum_reflection_details(patterns))
