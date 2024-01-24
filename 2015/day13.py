'''
Find the optimal seating arrangement witht the highest change in happiness points
'''

from collections import deque


def generate_all_seating_permutations(people, people_arrangement_map):
    """Generate all permutations of seating arrangement and determine the best"""
    permutations = deque()
    permutations.append([])

    best_happiness_points = 0

    for person in people:
        n = len(permutations)

        for _ in range(n):
            old_permutation = permutations.popleft()

            for j in range(len(old_permutation) + 1):
                # make a copy of old permutation
                # create a new permutation by adding the current person at every
                # position
                new_permutation = list(old_permutation)
                new_permutation.insert(j, person)

                if len(new_permutation) == len(people):
                    # We have a full arrangement involving all people
                    current_happiness_points = 0
                    new_permutation.append(new_permutation[0])

                    for i in range(len(new_permutation) - 1):
                        first_person = new_permutation[i]
                        second_person = new_permutation[i + 1]

                        current_happiness_points += people_arrangement_map[(
                            first_person, second_person)]
                        current_happiness_points += people_arrangement_map[(
                            second_person, first_person)]
                    best_happiness_points = max(
                        best_happiness_points, current_happiness_points)
                else:
                    permutations.append(new_permutation)
    return best_happiness_points


def find_optimal_happiness_points(lines, include_me):
    '''
    Find the optimal seating arrangement witht the highest change in happiness points
    '''

    people = set()
    people_arrangement_map = {}

    # Build a dictionary with key of tuple(person1, person2)
    # and the value being the points they gain or lose
    for line in lines:
        first_person, operation_second_person = line.split(" would ")
        operation_points, second_person = operation_second_person.split(
            " happiness units by sitting next to ")

        operation, points = operation_points.split(" ")

        second_person = second_person[:-1]

        if operation == "gain":
            points = int(points)
        else:
            points = -int(points)

        people_arrangement_map[(first_person, second_person)] = points
        if include_me:
            people_arrangement_map[(first_person, "Me")] = 0
            people_arrangement_map[("Me", first_person)] = 0

        people.add(first_person)
        people.add(second_person)

    if include_me:
        people.add("Me")

    return generate_all_seating_permutations(people, people_arrangement_map)


with open("day13_test.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    print(find_optimal_happiness_points(content, False))

    # Part 2 - include myself
    print(find_optimal_happiness_points(content, True))

with open("day13_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    print(find_optimal_happiness_points(content, False))
        # Part 2 - include myself
    print(find_optimal_happiness_points(content, True))
