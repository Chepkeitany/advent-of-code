extended_ascii_dict = {chr(i): i for i in range(256)}

def calculate_hash(string):
    hash = 0
    for char in string:
        hash += extended_ascii_dict[char]
        hash *= 17
        hash %= 256

    return hash

def sum_focusing_power_of_lens_config(input):
    # Initialize the 256 boxes with empty dictionaries
    boxes = [{} for i in range(256)]
    for string in input:
        # Split the string into the label and the operation
        # if the operation is an equals sign, it will be followed by a number indicating the focal length of the lens that needs to go into the relevant box
        last_value = string[-1]

        if (last_value == '-'):
            # This is a dash, so we need to remove the lens with the given label if it is present in the box
            # remove the lens with the given label if it is present in the box
            # move any remaining lenses as far forward in the box as they can go without changing their order, filling any space made by removing the indicated lens
            # Extract the label from the string
            label = string[:-1]
            # print("After ", string)
            hash_value = calculate_hash(label)
            # Get the box where the lens is located
            box = boxes[hash_value]
            if (label in box):
                # Remove the lens from the box
                box.pop(label)
                # Move the remaining lenses forward in the box
            # print(boxes)
        else:
            # This is an equals sign, so we need to add the lens to the box immediately behind any lenses already in the box
            # Don't move any of the other lenses when you do this
            # If there aren't any lenses in the box, the new lens goes all the way to the front of the box
            label = string[:-2]
            # print("After ", string)
            focal_length = string[-1]
            hash_value = calculate_hash(label)
            # Get the box where the lens is located
            box = boxes[hash_value]
            if (label in box):
                # Replace the old lens with the new lens
                # remove the old lens and put the new lens in its place, not moving any other lenses in the box
                box[label] = focal_length
            else:
                # Add the lens to the box
                box[label] = focal_length

            # print(boxes)
   
    total_focusing_power = 0

    for box in boxes:
        # skip if the box is empty
        if (len(box) == 0):
            continue
        for label, focal_length in box.items():
            # print(label, focal_length)
            box_number = calculate_hash(label)
            slot_number = list(box.keys()).index(label) + 1
            # print(label, box_number, slot_number, focal_length)
            total_focusing_power += (box_number + 1) * slot_number * int(focal_length)

    return total_focusing_power

file = open("day15_all.txt", "r")
content = file.read()
content = content.split(",")

print(sum_focusing_power_of_lens_config(content))
