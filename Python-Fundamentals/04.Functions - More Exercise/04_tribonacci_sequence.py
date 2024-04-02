number = int(input())


def tribonacci_sequence(def_num):
    sequence = [1]
    for i in range(1, def_num):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return ' '.join([str(num) for num in sequence])


print(tribonacci_sequence(number))