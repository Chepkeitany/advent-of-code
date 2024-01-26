'''
Find the fastest reindeer after a given distance.
Each reindeer flies at a certain speed then rests.
'''


def find_leading_reindeer(reindeer_state):
    leading_reindeer = None
    leading_distance = 0

    for name in reindeer_state:
        if reindeer_state[name]["current_distance"] > leading_distance:
            leading_reindeer = name
            leading_distance = reindeer_state[name]["current_distance"]

    return leading_reindeer, leading_distance


def find_highest_points(reindeer_state):
    leading_points = 0

    for name in reindeer_state:
        if reindeer_state[name]["current_points"] > leading_points:
            leading_points = reindeer_state[name]["current_points"]

    return leading_points


def find_winning_points(lines, time_elapsed):
    '''Find the reindeer that has travelled the farthest distance after a given time has elapsed'''
    reindeer_map = {}
    reindeer_state = {}
    for line in lines:
        name, action = line.split(" can fly ")
        flying, resting = action.split(" seconds, but then must rest for ")
        flying_speed, flying_duration = flying.split(" km/s for ")
        resting_duration, _ = resting.split(" ")

        flying_duration = int(flying_duration)
        flying_speed = int(flying_speed)
        resting_duration = int(resting_duration)

        reindeer_map[name] = (flying_speed, flying_duration, resting_duration)
        reindeer_state[name] = {
            "current_state": "flying",
            "current_points": 0,
            "current_distance": 0,
            "num_flying_seconds": 0,
            "num_resting_seconds": 0
        }

    for i in range(1, time_elapsed + 1):
        for reindeer_name in reindeer_map:
            reindeer_current_state = reindeer_state[reindeer_name]
            if reindeer_current_state["current_state"] == "flying":
                reindeer_current_state["current_distance"] += reindeer_map[reindeer_name][0]

                reindeer_current_state["num_flying_seconds"] += 1
                if reindeer_current_state["num_flying_seconds"] == reindeer_map[reindeer_name][1]:
                    reindeer_current_state["num_flying_seconds"] = 0
                    reindeer_current_state["current_state"] = "resting"

            else:
                reindeer_current_state["num_resting_seconds"] += 1
                if reindeer_current_state["num_resting_seconds"] == reindeer_map[reindeer_name][2]:
                    reindeer_current_state["num_resting_seconds"] = 0
                    reindeer_current_state["current_state"] = "flying"

        leading_reindeer, leading_distance = find_leading_reindeer(
            reindeer_state)

        reindeer_state[leading_reindeer]["current_points"] += 1

    return find_highest_points(reindeer_state)


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

    assert find_winning_points(
        content, 1000) == 688, "Failed on test input - part 2"


with open("day14_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()

    assert find_winning_distance(
        content, 2503) == 2655, "Failed on main input - part1"
    assert find_winning_points(
        content, 2503) == 1059, "Failed on main input - part2"

    print("All tests passed!")
