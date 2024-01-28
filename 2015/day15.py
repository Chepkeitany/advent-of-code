'''
Finding highest-scoring cookie using the combinations
of each of the given ingredients
'''


def find_highest_score(lines, include_calorie_check):
    """Find the highest score"""
    ingredient_property_map = {}
    for line in lines:
        ingredient, properties = line.split(": ")
        properties = properties.split(", ")
        properties_map = {}
        for prop in properties:
            prop, quantity = prop.split(" ")
            properties_map[prop] = int(quantity)

        ingredient_property_map[ingredient] = properties_map

    highest_score = 0
    for i in range(1, 100):
        for j in range(1, 100):
            for k in range(1, 100):
                for l in range(1, 100):
                    if i + j + k + l != 100:
                        continue
                    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
                    ingredient_1 = ingredient_property_map["Frosting"]
                    capacity += ingredient_1["capacity"] * i
                    durability += ingredient_1["durability"] * i
                    flavor += ingredient_1["flavor"] * i
                    texture += ingredient_1["texture"] * i
                    calories += ingredient_1["calories"] * i

                    ingredient_2 = ingredient_property_map["Candy"]

                    capacity += ingredient_2["capacity"] * j
                    durability += ingredient_2["durability"] * j
                    flavor += ingredient_2["flavor"] * j
                    texture += ingredient_2["texture"] * j
                    calories += ingredient_2["calories"] * j

                    ingredient_3 = ingredient_property_map["Butterscotch"]

                    capacity += ingredient_3["capacity"] * k
                    durability += ingredient_3["durability"] * k
                    flavor += ingredient_3["flavor"] * k
                    texture += ingredient_3["texture"] * k
                    calories += ingredient_3["calories"] * k

                    ingredient_4 = ingredient_property_map["Sugar"]

                    capacity += ingredient_4["capacity"] * l
                    durability += ingredient_4["durability"] * l
                    flavor += ingredient_4["flavor"] * l
                    texture += ingredient_4["texture"] * l
                    calories += ingredient_4["calories"] * l

                    if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
                        continue
                    current_score = capacity * durability * flavor * texture
                
                    if include_calorie_check:
                        if calories == 500 and current_score > highest_score:
                            highest_score = current_score
                    else:
                        if current_score > highest_score:
                            highest_score = current_score

    return highest_score


if __name__ == "__main__":
    with open("day15_all.txt", encoding="utf-8") as file:
        content = file.read().splitlines()
        assert find_highest_score(content, False) == 18965440, "Failed on main input - part1"

        assert find_highest_score(content, True) == 15862900, "Failed on main input - part2"

        print("All tests passed!")
