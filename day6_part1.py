def find_all_ways_to_win(time_distance):
    _, times = time_distance[0].split(":")
    times = times.strip().split(" ")
    times = [item for item in times if item]

    _, distances = time_distance[1].split(":")
    distances = distances.strip().split(" ")
    distances = [item for item in distances if item]
    total_ways = 1


    for i, time in enumerate(times):
        time = int(time)
        ways_to_win = 0
        distance = int(distances[i])
        # print(time, distance)
        for j in range(0, time + 1):
            race_time = time - j
            distance_covered = j * race_time
            # print(distance_covered)
            if (j * race_time) > distance:
                ways_to_win += 1
        # print(ways_to_win)
        total_ways *= ways_to_win

    return total_ways


# Read the seeds to soil map
file = open("day6_all.txt", "r")
content = file.read()
time_distance = content.split("\n")

print(find_all_ways_to_win(time_distance))
