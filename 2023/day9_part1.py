def sum_next_number_in_sequence(sequences):
    sum = 0

    for sequence in sequences:
        sequence = sequence.split(" ")
        sequence = [int(i) for i in sequence]

        # Make a new sequence from the difference at each step of your history
        # Once all of the values in your latest sequence are zeroes, you can extrapolate what the next value of the original history should be
        # work out the next value in each sequence from the bottom up:
        all_zeroes = False
        temp_sequences = [sequence]
        while not all_zeroes:
            new_sequence = []
            for i in range(len(sequence) - 1):
                new_sequence.append(int(sequence[i + 1]) - int(sequence[i]))

            temp_sequences.append(new_sequence)

            # If that sequence is not all zeroes, repeat this process, using the sequence you just generated as the input sequence
            if new_sequence[len(new_sequence) - 1] == 0:
                all_zeroes = True
            else:
                sequence = new_sequence

        # Starting from last sequence, work out the next value in each sequence from the bottom up
        next_number = 0
        for i in range(len(temp_sequences) - 1, -1, -1):
            temp_sequence = temp_sequences[i]
            next_number += temp_sequence[len(temp_sequence) - 1]
        #print(next_number)
        sum += next_number
    return sum


with open("day9_all.txt") as file:
    lines = file.read().split("\n")

print(sum_next_number_in_sequence(lines))
