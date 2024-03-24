sequence_numbers = list(map(float, input().split(" ")))
absolute_value = []
for num in sequence_numbers:
    absolute_value.append(abs(num))
print(absolute_value)