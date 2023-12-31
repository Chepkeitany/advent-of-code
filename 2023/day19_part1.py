def calculate_accepted_parts_ratings(workflows, parts):
    ratings = 0
    # Parse the workflows into a dictionary of key = workflow name, value = list of rules
    workflow_rules = {}
    for workflow in workflows:
        # The part before the first { is the workflow name
        workflow_name = workflow.split('{')[0].strip()
        # print(workflow_name)
        # The part after the first { is the list of rules excluding the last }
        rules = workflow.split('{')[1].strip()[:-1].split(',')
        rules_as_dict = []
        # Parse the rules into a dictionary of key = rule condition, value = rule destination for easy lookup when processing parts
        for rule in rules:
            # print(rule)
            rule_condition = rule.split(':')
            if len(rule_condition) == 1:
                # This is the last rule in the workflow, it has no condition
                rules_as_dict.append((rule_condition[0]))
            else:
                category = rule_condition[0][0]
                comparator = rule_condition[0][1]
                value = int(rule_condition[0][2:])

                rule_destination = rule_condition[1]
                rules_as_dict.append((category, comparator, value, rule_destination))
        workflow_rules[workflow_name] = rules_as_dict

    # Parse the parts into a dictionary of key = part name, value = part ratings
    for part in parts:
        part_details = part[1:-1].split(',')
        part_category_ratings = {}
        for part_detail in part_details:
            category = part_detail[0]
            value = int(part_detail[2:])
            part_category_ratings[category] = value

        # Process the part through the workflows, starting from the workflow named 'in'
        current_workflow = 'in'
        
        part_fully_processed = False
        while not part_fully_processed:
            if current_workflow not in workflow_rules:
                if current_workflow == 'A':
                    # print('Part accepted')
                    ratings += sum(part_category_ratings.values())
                    part_fully_processed = True
                    break
                elif current_workflow == 'R':
                    # print('Part rejected')
                    part_fully_processed = True
                    break
            for rule in workflow_rules[current_workflow]:
                if type(rule) == str:
                    if rule == 'A':
                        # print('Part accepted')
                        ratings += sum(part_category_ratings.values())
                        part_fully_processed = True
                        break
                    elif rule == 'R':
                        # print('Part rejected')
                        part_fully_processed = True
                        break
                    else:
                        current_workflow = rule
                else:
                    category, comparator, value, destination = rule
                    if comparator == '<':
                        if part_category_ratings[category] < value:
                            current_workflow = destination
                            break
                    elif comparator == '>':
                        if part_category_ratings[category] > value:
                            current_workflow = destination
                            break

    return ratings

# Read in the input file day19_test.txt and get the list of workflows and parts
with open('day19_all.txt') as f:
    workflows = []
    parts = []
    for line in f:
        if line.strip() == '':
            continue
        elif line.strip().startswith('{'):
            parts.append(line.strip())
        else:
            workflows.append(line.strip())

total_ratings = calculate_accepted_parts_ratings(workflows, parts)
print(total_ratings)
