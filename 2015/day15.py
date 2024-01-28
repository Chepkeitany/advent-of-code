'''
Finding highest-scoring cookie using the combinations
of each of the given ingredients
'''


def parse_properties(property_str):
    """Parse a string of properties into a dictionary."""
    properties = {}
    for prop in property_str.split(", "):
        key, value = prop.split(" ")
        properties[key] = int(value)
    return properties


def calculate_property_scores(ingredient_amounts, ingredient_property_map):
    """Calculate the total scores for each property based on ingredient amounts."""
    total_properties = {
        prop: 0 for prop in ingredient_property_map[next(iter(ingredient_property_map))]}
    for ingredient, amount in ingredient_amounts.items():
        for prop, value in ingredient_property_map[ingredient].items():
            total_properties[prop] += value * amount
    return total_properties


def generate_combinations(ingredients, total, current_combination):
    """
    Recursively generate all possible combinations of
    ingredient amounts that sum up to a total.
    """
    if len(current_combination) == len(ingredients):
        if sum(current_combination) == total:
            yield current_combination
        return

    start = 1 if not current_combination else 0
    for amount in range(start, total - sum(current_combination) + 1):
        yield from generate_combinations(ingredients, total, current_combination + [amount])


def find_highest_score(lines, include_calorie_check):
    """Find the highest score for a dynamic number of ingredients."""
    ingredient_property_map = {
        line.split(": ")[0]: parse_properties(
            line.split(": ")[1]) for line in lines}
    ingredients = list(ingredient_property_map.keys())

    highest_score = 0
    for combination in generate_combinations(ingredients, 100, []):
        ingredient_amounts = dict(zip(ingredients, combination))
        total_properties = calculate_property_scores(
            ingredient_amounts, ingredient_property_map)

        if any(value <= 0 for value in total_properties.values()
               if value != total_properties.get("calories", 0)):
            continue

        current_score = 1
        for prop, value in total_properties.items():
            if prop != "calories":
                current_score *= value

        if include_calorie_check and total_properties.get(
                "calories", 0) != 500:
            continue

        highest_score = max(highest_score, current_score)

    return highest_score


if __name__ == "__main__":
    with open("day15_all.txt", encoding="utf-8") as file:
        content = file.read().splitlines()
        assert find_highest_score(
            content, False) == 18965440, "Failed on main input - part1"

        assert find_highest_score(
            content, True) == 15862900, "Failed on main input - part2"

        print("All tests passed!")
