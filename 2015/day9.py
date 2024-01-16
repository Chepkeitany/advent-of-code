'''
We're given the routes between two cities and their distances.

# Part 1
Calculate shortest distance that ensures that we visit all locations at least once
'''

from collections import deque


def find_shortest_distance_to_all_cities(lines):
    """Calculate shortest distance to all cities"""
    routes_cost = {}
    cities = set()

    for line in lines:
        route, cost = line.split(" = ")
        city1, city2 = route.split(" to ")
        routes_cost[(city1, city2)] = int(cost)
        routes_cost[(city2, city1)] = int(cost)

        cities.add(city1)
        cities.add(city2)

    # Build permutations of all the cities and
    # keep track of the permutation with the shortest distance
    shortest_distance = float("inf")
    num_cities = len(cities)
    permutations = deque()
    permutations.append([])
    for city in cities:
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
                if len(new_permutation) == num_cities:
                    journey_cost = 0
                    # Calculate distance of using this route
                    for i in range(len(new_permutation) - 1):
                        route = (new_permutation[i], new_permutation[i + 1])
                        journey_cost += routes_cost[route]
                    shortest_distance = min(shortest_distance, journey_cost)
                else:
                    permutations.append(new_permutation)
    return shortest_distance


with open("day9_test.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    assert find_shortest_distance_to_all_cities(
        content) == 605, "Failed on test input - part1"

with open("day9_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    assert find_shortest_distance_to_all_cities(
        content) == 141, "Failed on main input - part1"

print("All tests passed!")
