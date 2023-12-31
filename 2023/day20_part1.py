def calculate_product_low_high_pulses(lines):
    # for i in range(1000):
        # Push the button 
        # Send a low pulse to broadcaster
        # Then follow through the modules
        # Count the number of low and high pulses
        # Multiply them together

        # Rules:
        # When a flip-flop module receives a high pulse, it does nothing and remembers that it received a high pulse.
        # When a flip-flop module receives a low pulse, it turns off and sends a high pulse to all of its destination modules, also remembering that it sent a high pulse.
        # When a conjunction module receives a high pulse, it remembers it and if all of its inputs are high, it sends a low pulse to all of its destination modules. Otherwise, it sends a high pulse
    module_state = {}
    conjunction_state = {}
    module_type = {}
    producer_receiver_map = {}
    receiver_producer_map = {}
    for line in lines:
        producer, receiver = line.split("->")
        receivers = receiver.strip().split(",")
        producer = producer.strip()
        receivers = [receiver.strip() for receiver in receivers]
        # Identify flip-flop and conjunction modules
        if producer.startswith("%"):
            producer = producer[1:]
            module_type[producer] = "flip-flop"
            module_state[producer] = False
            producer_receiver_map[producer] = receivers
            # print("Flip-flop module")
        elif producer.startswith("&"):
            producer = producer[1:]
            module_type[producer] = "conjunction"
            module_state[producer] = False
            producer_receiver_map[producer] = receivers
            # print("Conjunction module")
        elif producer == "broadcaster":
            producer = producer
            # print("Broadcaster module")
            producer_receiver_map[producer] = receivers
        else:
            # print("Untyped module")
            producer_receiver_map[producer] = receivers

        for receiver in receivers:
            if receiver in receiver_producer_map:
                receiver_producer_map[receiver].append(producer)
            else:
                receiver_producer_map[receiver] = [producer]


    # print(producer_receiver_map)
    # print(receiver_producer_map)
    # print(module_type)
    count_high_pulses = 0
    count_low_pulses = 0
    
    for i in range(1000):
        #New push of the button
        # print("Pushing the button ", i  + 1, " time")
        queue = [("low", "broadcaster")]
        while len(queue) > 0:
            pulse, producer = queue.pop(0)
            # print(pulse, producer)
            receivers = []
            if producer in producer_receiver_map:
                receivers = producer_receiver_map[producer]
            if pulse == "low":
                count_low_pulses += 1
            else:
                count_high_pulses += 1
            if producer in producer_receiver_map:
                if producer == "broadcaster":
                    for receiver in receivers:
                        queue.append((pulse, receiver))

                if producer in module_type:
                        if module_type[producer] == "flip-flop":
                            if pulse == "low":
                                if not module_state[producer]:
                                    module_state[producer] = True
                                    pulse = "high"
                                else:
                                    module_state[producer] = False
                                    pulse = "low"
                                for receiver in receivers:
                                    queue.append((pulse, receiver))
                        elif module_type[producer] == "conjunction":
                            # Check the state of the inputs of this conjunction
                            # If all inputs are high, send a low pulse to all of its destination modules
                            conjunction_state[producer] = pulse
                 
                            inputs = receiver_producer_map[producer]
                            # Check the states of the inputs
                            all_inputs_high = True
                            for input in inputs:
                                if not module_state[input]:
                                    all_inputs_high = False
                                    break
                            if all_inputs_high:
                                pulse = "low"
                            else:
                                pulse = "high"
                            # The state of the conjunction module is the & of the states of all its inputs
                            if (pulse == "high"):
                                module_state[producer] = True
                            else:
                                module_state[producer] = False
                            for receiver in receivers:
                                queue.append((pulse, receiver))

            else:
                for receiver in receivers:
                    queue.append((pulse, receiver))

    print("Low pulses: ", count_low_pulses)
    print("High pulses: ", count_high_pulses)
    print("Product: ", count_low_pulses * count_high_pulses)

file = open("day20_all.txt", "r")
content = file.read()
content = content.split("\n")
result = calculate_product_low_high_pulses(content)
