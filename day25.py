import networkx as nx
from graphviz import Graph

def compute_connected_components_product(lines):
    # remove duplicate edges
    graph = []
    for line in lines:
        line = line.strip().split(":")
        component = line[0].strip()
        connected_components = [item.strip() for item in line[1].split()]

        for connected_component in connected_components:
            graph.append((component, connected_component))


    #### Code to visualize the graph ####
    # Create a new graph
    # dot = Graph(comment='My Graph')

    # for start, end in graph:
    #     dot.edge(start, end)

    # # Save and render the graph to a file (e.g., in PNG format)
    # dot.render('my-graph.gv', format='png', view=True)

    # print(graph)

    G = nx.Graph()

    G.add_edges_from(graph)

    # Compute the minimum number of edges to remove to make the graph disconnected
    edges_to_remove = nx.minimum_edge_cut(G)

    # Remove the edges in the edge cut
    G.remove_edges_from(edges_to_remove)

    # Find connected components
    components = list(nx.connected_components(G))

    # print(components)

    edges_in_connected_components = [len(component) for component in components]

    #print("Edges in each component:", edges_in_connected_components)

    components_group1_count, components_group2_count = edges_in_connected_components

    result = components_group1_count * components_group2_count

    return result
    
file = open("day25_all.txt", "r")
content = file.read()
lines = content.split("\n")
result = compute_connected_components_product(lines)
print(result)
