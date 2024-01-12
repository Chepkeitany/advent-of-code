'''
Calculate the signals for a given wire after a series of bitwise instructions
'''
def map_wire_to_operation(lines, wire_operation_map):
    """Create a map of wire to the operation for that wire"""
    for line in lines:
        operation, wire = line.split(' -> ')
        wire_operation_map[wire] = operation


def calculate_wire_signal(wire, results):
    """Calculate the value of the wire after running through some instructions"""
    try:
        return int(wire)
    except ValueError:
        pass

    if wire not in results:
        operation = wire_operation_map[wire].split(" ")

        if "NOT" in operation:
            result = ~calculate_wire_signal(operation[1], results) & 0xffff
        elif "AND" in operation:
            result = calculate_wire_signal(
                operation[0], results) & calculate_wire_signal(
                operation[2], results)
        elif "OR" in operation:
            result = calculate_wire_signal(
                operation[0], results) | calculate_wire_signal(
                operation[2], results)
        elif "LSHIFT" in operation:
            result = calculate_wire_signal(
                operation[0], results) << calculate_wire_signal(
                operation[2], results)
        elif "RSHIFT" in operation:
            result = calculate_wire_signal(
                operation[0], results) >> calculate_wire_signal(
                operation[2], results)
        else:
            result = calculate_wire_signal(operation[0], results)
        results[wire] = result
    return results[wire]


with open("day7_all.txt", encoding="utf-8") as file:
    content = file.read().splitlines()
    wire_operation_map = {}
    map_wire_to_operation(content, wire_operation_map)

    # Part 1
    results = {}
    assert calculate_wire_signal("a", results) == 956, "Failed part 1"

    results = {'b': 956}
    assert calculate_wire_signal("a", results) == 40149, "Failed part 2"

    print("All tests passed!")
