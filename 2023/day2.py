import re

# Configuration: 12 red cubes, 13 green cubes, and 14 blue cubes
red = 12
green = 13
blue = 14

def extract_number_and_word(s):
    # Find the first occurrence of a pattern with digits followed by non-digits
    match = re.search(r'(\d+)\s*([^\d]+)', s)
    if match:
        num, word = match.groups()
        return [int(num), word.strip()]
    else:
        return None

def solve(games):
    sum_ids = 0
    total_power_set = 0
    for game in games:
        game_details = game.split(":")
        game = game_details[1]
        game_id = game_details[0].split(" ")[1]
        # print(game_id)
        game_sets = game.split(";")
        is_game_possible = True
        minimum_red = -1
        minimum_green = -1
        minimum_blue = -1
        for game_set in game_sets:
            game_set = game_set.split(",")
            red_set = 0
            green_set = 0
            blue_set = 0
            for cube in game_set:
                cube = cube.strip()
                result = extract_number_and_word(cube)
                if result is not None:
                    if result[1] == "red":
                        red_set += int(result[0])
                    if result[1] == "green":
                        green_set += int(result[0])
                    if result[1] == "blue":
                        blue_set += int(result[0])

            if red_set > minimum_red:
                minimum_red = red_set
            if green_set > minimum_green:
                minimum_green = green_set
            if blue_set > minimum_blue:
                minimum_blue = blue_set

            if red_set > red or green_set > green or blue_set > blue:
                #print(red_set, green_set, blue_set)
                is_game_possible = False
        if is_game_possible:
            sum_ids += int(game_id)
        minimum_power_set = minimum_red * minimum_green * minimum_blue
        print(minimum_power_set)
        total_power_set += minimum_power_set
    return sum_ids, total_power_set
                
# print(solve(games))

# Read the puzzle input
file = open("day2_all.txt", "r")
content = file.read()
print(solve(content.split("\n")))
file.close()
