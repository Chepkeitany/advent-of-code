'''
We're given the routes between two locations and their distances.
You can start and end at any two (different) locations and must visit each location exactly once

# Part 1
Calculate shortest distance that ensures that we visit each location exactly once

# Part 2
Calculate longest distance that ensures that we visit each location exactly once
'''

from collections import deque

def calculate_permutations_and_distance(locations, routes_cost):
    """Generate permutations and calculate distance for that routes"""
    shortest_distance = float("inf")
    longest_distance = float("-inf")
    num_locations = len(locations)
    permutations = deque()
    permutations.append([])
    for city in locations:
        # we will take all existing permutations and add the current city to create
        # new permutations
        n = len(permutations)
        for _ in range(n):
            old_permutation = permutations.popleft()
            # create a new permutation by adding the current city at every
            # position
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, city)
                if len(new_permutation) == num_locations:
                    journey_cost = 0
                    # Calculate distance of using this route
                    for i in range(len(new_permutation) - 1):
                        route = (new_permutation[i], new_permutation[i + 1])
                        journey_cost += routes_cost[route]
                    shortest_distance = min(shortest_distance, journey_cost)
                    longest_distance = max(longest_distance, journey_cost)
                else:
                    permutations.append(new_permutation)

    return shortest_distance, longest_distance
def find_distance_to_all_locations(lines):
    """Calculate shortest distance to all locations"""
    routes_cost = {}
    locations = set()

    for line in lines:
        route, cost = line.split(" = ")
        city1, city2 = route.split(" to ")
        routes_cost[(city1, city2)] = int(cost)
        routes_cost[(city2, city1)] = int(cost)

        locations.add(city1)
        locations.add(city2)

    # Build permutations of all the locations and
    # keep track of the permutation with the shortest distance

    return calculate_permutations_and_distance(locations, routes_cost)

with open("day9_test.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    shortest_distance, longest_distance = find_distance_to_all_locations(
        content)

    assert shortest_distance == 605, "Failed on test input - part1"
    assert longest_distance  == 982, "Failed on test input - part2"

with open("day9_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()
    shortest_distance, longest_distance = find_distance_to_all_locations(
        content)
    assert shortest_distance == 141, "Failed on main input - part1"
    assert longest_distance  == 736, "Failed on test input - part2"

print("All tests passed!")
