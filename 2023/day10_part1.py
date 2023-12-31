pipe_connectivity_dictionary = {
    "F": ["s", "e"],
    "|": ["n", "s"],
    "-": ["e", "w"],
    "7": ["s", "w"],
    "J": ["n", "w"],
    "L": ["n", "e"],
    "S": ["n", "s", "e", "w"] # For s we can't guess the direction so we have to try all the directions
}

opposite_directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

def convert_input_to_graph(input):
    graph = []
    for line in input:
        graph.append(list(line))
    return graph 

def find_starting_node(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == "S":
                return (i, j)

file = open("day10_all.txt", "r")
content = file.read()
graph_input = content.split("\n")

graph = convert_input_to_graph(graph_input)
starting_node = find_starting_node(graph)

# We can use BFS to find the farthest node from the starting node
def find_farthest_node_from_start(graph, starting_node):
    queue = []
    queue.append([starting_node, 0])
    visited = dict()
    distance_to_farthest_node_in_loop = 0
    while queue:
        current_node, distance = queue.pop(0) # remove the first element from the list

        if current_node in visited:
            continue

        visited[current_node] = distance
        if distance > distance_to_farthest_node_in_loop:
            distance_to_farthest_node_in_loop = distance
        row, col = current_node
        available_directions = pipe_connectivity_dictionary[graph[row][col]]
        for direction in available_directions:
            row_change, col_change, opposite_direction = opposite_directions[direction]
            new_row = row + row_change
            new_col = col + col_change

            if (new_row < 0 or new_row >= len(graph)) or (new_col < 0 or new_col >= len(graph[0])):
                continue

            target = graph[new_row][new_col]
            if target not in pipe_connectivity_dictionary:
                continue

            target_directions = pipe_connectivity_dictionary[target]

            if opposite_direction in target_directions:
                queue.append([(new_row, new_col), distance + 1])

    return distance_to_farthest_node_in_loop

print(find_farthest_node_from_start(graph, starting_node))
