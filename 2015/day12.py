'''
Extract numbers from nested json objects and lists
'''
import json

def flatten(content):
    """Flatten the json object into actual values"""
    if isinstance(content, int):
        return content
    if isinstance(content, list):
        return sum([flatten(item) for item in content])
    if not isinstance(content, dict):
        return 0
    # Convert the values of the dictionary into a list
    return flatten(list(content.values()))

# Open the file and read its contents
with open('day12_all.txt', encoding="utf-8") as file:
    file_content = file.read()

    # Convert the file content to a JSON object
    json_object = json.loads(file_content)
    # print(flatten(json_object))
    assert flatten(json_object) == 111754, "Failed on main input - part1"
