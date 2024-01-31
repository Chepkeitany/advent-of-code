'''
Find the number of ways to store a given amount of eggnog into
the given number of containers
'''

from itertools import combinations


def num_combinations(amount, containers):
    '''Find the number of combinations of containers that sum up to given amount'''
    result = []
    for number_of_containers in range(1, len(containers) + 1):
        for combination in combinations(containers, number_of_containers):
            if sum(combination) == amount:
                result.append(combination)

    return result


if __name__ == "__main__":
    # Test input
    test_input_result = (num_combinations(25, [20, 15, 10, 5, 5]))
    assert len(test_input_result) == 4, "Failed on test input - part 1"

    # Main input
    with open("day17_all.txt", encoding="utf-8") as f:
        content = f.read().splitlines()

        content = [int(x) for x in content]

        main_input_result = num_combinations(150, content)
        assert len(main_input_result) == 1638, "Failed on main input - part 1"

        min_number_containers = len(
            min(main_input_result, key=lambda x: len(x)))
        num_ways_with_min_containers = sum(
            1 for combination in main_input_result if len(combination) == min_number_containers)
        assert num_ways_with_min_containers == 17, "Failed on main input - part 2"

        print("All tests passed!")
