'''
Find the fastest reindeer after a given distance.
Each reindeer flies at a certain speed then rests.
'''


def find_winning_distance(lines, time_elapsed):
    '''Find the reindeer that has travelled the farthest distance after a given time has elapsed'''
    fastest_distance = 0
    for line in lines:
        _, action = line.split(" can fly ")
        flying, resting = action.split(" seconds, but then must rest for ")
        flying_speed, flying_duration = flying.split(" km/s for ")
        resting_duration, _ = resting.split(" ")

        flying_duration = int(flying_duration)
        flying_speed = int(flying_speed)
        resting_duration = int(resting_duration)

        total_distance = 0
        remaining_time = time_elapsed
        while remaining_time > 0:
            if remaining_time < flying_duration:
                total_distance += remaining_time * flying_speed
                break
            remaining_time -= flying_duration
            total_distance += flying_duration * flying_speed
            if remaining_time >= resting_duration:
                remaining_time -= resting_duration
            else:
                break

        if total_distance > fastest_distance:
            fastest_distance = total_distance
    return fastest_distance


with open("day14_test.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    assert find_winning_distance(
        content, 1000) == 1120, "Failed on test input - part 1"

with open("day14_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    assert find_winning_distance(
        content, 2503) == 2655, "Failed on main input - part1"

    print("All tests passed!")
