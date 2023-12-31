from collections import deque


def sum_shortest_paths_between_pairs_of_galaxies(galaxies):
    # Each pair of galaxies should only considered once

    # Some constraints:
    # any rows or columns that contain no galaxies should all actually be twice as big.

    # 1. Update the graph to insert extra rows for the rows that contain no galaxies
    doubled_rows_where_no_galaxies = add_extra_rows(galaxies)
    # print(doubled_rows_where_no_galaxies)

    # 2. Update the graph to insert extra columns for the columns that contain no galaxies
    doubled_cols_where_no_galaxies = add_extra_cols(doubled_rows_where_no_galaxies)
    # print(doubled_cols_where_no_galaxies)

    # 3. Find and rename all the galaxies from 1 to n
    numbered_graph, largest_galaxy_number, galaxy_positions = rename_galaxies(doubled_cols_where_no_galaxies)
    # print(numbered_graph)

    # 4. Find and sum the shortest paths between each pair of galaxies
    shortest_paths_sum = find_and_sum_shortest_paths(numbered_graph, largest_galaxy_number, galaxy_positions)
    print(shortest_paths_sum)
def rename_galaxies(galaxies):
    # 1. Find and rename all the galaxies from 1 to n
    galaxy_positions = { }
    galaxy_number = 1
    for row in range(len(galaxies)):
        for col in range(len(galaxies[row])):
            if galaxies[row][col] == "#":
                galaxies[row][col] = galaxy_number
                galaxy_positions[galaxy_number] = (row, col)
                galaxy_number += 1
    return galaxies, galaxy_number, galaxy_positions

def add_extra_rows(galaxies):
    # 1. Mutate the graph to insert extra rows for the rows that contain no galaxies
    graph_doubled_rows = []
    for i, row in enumerate(galaxies):
        if "#" in galaxies[i]:
            graph_doubled_rows.append(row)
        else:
            graph_doubled_rows.append(row)
            graph_doubled_rows.append(row)

    return graph_doubled_rows

def add_extra_cols(galaxies):
    # 2. Mutate the graph to double the that contain no galaxies
    # Transpose the matrix to work with columns
    transposed = list(zip(*galaxies))

    # Determine columns without '@'
    cols_without_at = [i for i, col in enumerate(transposed) if '#' not in col]

    # Create a new matrix with doubled columns where needed
    new_transposed = []
    for i, col in enumerate(transposed):
        new_transposed.append(col)
        if i in cols_without_at:
            new_transposed.append(col)  # Add the column again if it's one of the columns without '@'

    # Transpose back to get the final matrix
    new_matrix = list(zip(*new_transposed))

    # Convert tuples back to lists (if needed)
    new_matrix = [list(row) for row in new_matrix]

    return new_matrix

def find_shortest_path(galaxies, start, end):
    # Use BFS to find the shortest path between two galaxies
    rows, cols = len(galaxies), len(galaxies[0])
    visited = set([start])
    queue = deque([(start, 0)]) # position, distance

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        position, distance = queue.popleft()
        row, col = position

        if position == end:
            return distance

        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append(((new_row, new_col), distance + 1))

    return -1 # No path found
    
def find_and_sum_shortest_paths(galaxies, largest_galaxy_number, galaxy_positions):
    # 4. Find the shortest path between each pair of galaxies
    # 5. Sum the shortest paths
    shortest_paths_sum = 0

    # pairs = 0
    for i in range(1, largest_galaxy_number):
        for j in range(i + 1, largest_galaxy_number):
            # pairs += 1
            shortest_path = find_shortest_path(galaxies, galaxy_positions[i], galaxy_positions[j])
            print(i, j, shortest_path)
            shortest_paths_sum += shortest_path
   
    return shortest_paths_sum

def convert_input_to_graph(input):
    graph = []
    for line in input:
        graph.append(list(line))
    return graph 


file = open("day11_all.txt", "r")
content = file.read()
graph_input = content.split("\n")

graph = convert_input_to_graph(graph_input)
sum_shortest_paths_between_pairs_of_galaxies(graph)
