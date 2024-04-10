def pokemon_dont_go(sequence):
    removed_sum = 0

    while sequence:
        try:
            index = int(input())
            if index < 0:
                index = 0
                sequence[0] = sequence[-1]
            elif index >= len(sequence):
                index = len(sequence) - 1
                sequence[-1] = sequence[0]

            removed_element = sequence.pop(index)
            removed_sum += removed_element

            for i in range(len(sequence)):
                if sequence[i] <= removed_element:
                    sequence[i] += removed_element
                else:
                    sequence[i] -= removed_element

        except EOFError:
            break

    return removed_sum


sequence = list(map(int, input().split()))
result = pokemon_dont_go(sequence)
print(result)