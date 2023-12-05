def calculate_lowest_location(seeds, seeds_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map):
    seeds = seeds.split(" ")

    lowest_location = float('inf')
    for seed in seeds:
        seed = int(seed)
        soil_destination = seed
        for line in seeds_to_soil_map:
            line = line.split(" ")
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])

            # Find if seed is in the source range
            if seed >= source_range_start and seed < source_range_start + range_length:
                # Find the destination location
                soil_destination = destination_range_start + (seed - source_range_start)
                break
        # print(soil_destination)

        fertilizer_destination = soil_destination
        for line in soil_to_fertilizer_map:
            line = line.split(" ")
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])

            # Find if seed is in the source range
            if soil_destination >= source_range_start and soil_destination < source_range_start + range_length:
                # Find the destination location
                fertilizer_destination = destination_range_start + (soil_destination - source_range_start)
                break
        # print(fertilizer_destination)

        water_destination = fertilizer_destination
        for line in fertilizer_to_water_map:
            line = line.split(" ")
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])

            # Find if seed is in the source range
            if fertilizer_destination >= source_range_start and fertilizer_destination < source_range_start + range_length:
                # Find the destination location
                water_destination = destination_range_start + (fertilizer_destination - source_range_start)
                break

        # print(water_destination)

        light_destination = water_destination
        for line in water_to_light_map:
            line = line.split(" ")
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])

            # Find if seed is in the source range
            if water_destination >= source_range_start and water_destination < source_range_start + range_length:
                # Find the destination location
                light_destination = destination_range_start + (water_destination - source_range_start)
                break

        # print(light_destination)
        temperature_destination = light_destination
        for line in light_to_temperature_map:
            line = line.split(" ")
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])

            # Find if seed is in the source range
            if light_destination >= source_range_start and light_destination < source_range_start + range_length:
                # Find the destination location
                temperature_destination = destination_range_start + (light_destination - source_range_start)
                break

        # print(temperature_destination)
        humidity_destination = temperature_destination
        for line in temperature_to_humidity_map:
            line = line.split(" ")
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])

            # Find if seed is in the source range
            if temperature_destination >= source_range_start and temperature_destination < source_range_start + range_length:
                # Find the destination location
                humidity_destination = destination_range_start + (temperature_destination - source_range_start)
                break

        # print(humidity_destination)

        location_destionation = humidity_destination
        for line in humidity_to_location_map:
            line = line.split(" ")
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])

            # Find if seed is in the source range
            if humidity_destination >= source_range_start and humidity_destination < source_range_start + range_length:
                # Find the destination location
                location_destionation = destination_range_start + (humidity_destination - source_range_start)
                break

        if location_destionation < lowest_location:
            lowest_location = location_destionation
    
    return lowest_location


# Read the seeds
file = open("all_seeds.txt", "r")
seeds = file.read()

# Read the seeds to soil map
file = open("all_seed_to_soil.txt", "r")
content = file.read()
seeds_to_soil_map = content.split("\n")

# Read the soil to fertilizer map
file = open("all_soil_to_fertilizer.txt", "r")
content = file.read()
soil_to_fertilizer_map = content.split("\n")

# Read fertilizer to water map
file = open("all_fertilizer_to_water.txt", "r")
content = file.read()
fertilizer_to_water_map = content.split("\n")

# Read the water-to-light map
file = open("all_water_to_light.txt", "r")
content = file.read()
water_to_light_map = content.split("\n")

# Read the light-to-temperature map
file = open("all_light_to_temperature.txt", "r")
content = file.read()
light_to_temperature_map = content.split("\n")

# Read the temperature-to-humidity map
file = open("all_temperature_to_humidity.txt", "r")
content = file.read()
temperature_to_humidity_map = content.split("\n")

# Read the humidity-to-location map
file = open("all_humidity_to_location.txt", "r")
content = file.read()
humidity_to_location_map = content.split("\n")


file.close()
result = calculate_lowest_location(seeds, seeds_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map)
print(result)
