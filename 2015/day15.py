'''
Finding highest-scoring cookie using the combinations
of each of the given ingredients
'''
def find_highest_score(lines):
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
        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
        ingredient_1 = ingredient_property_map["Butterscotch"]
        capacity += ingredient_1["capacity"] * i
        durability += ingredient_1["durability"] * i
        flavor += ingredient_1["flavor"] * i
        texture += ingredient_1["texture"] * i
        calories += ingredient_1["calories"] * i

        for j in range(100 - i, 1, -1):
            if i + j != 100:
                continue
            ingredient_2 = ingredient_property_map["Cinnamon"]

            capacity += ingredient_2["capacity"] * j
            durability += ingredient_2["durability"] * j
            flavor += ingredient_2["flavor"] * j
            texture += ingredient_2["texture"] * j
            calories += ingredient_2["calories"] * j

            if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0 or calories <= 0:
                continue

            current_score = capacity * durability * flavor * texture

            if current_score > highest_score:
                highest_score = current_score

    return highest_score

if __name__ == "__main__":
    with open("day15_test.txt", encoding="utf-8") as file:
        content = file.read().splitlines()
        print(find_highest_score(content))
