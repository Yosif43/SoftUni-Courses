n = int(input())
positives = []
negatives = []
for integer in range(n):
    user_input = int(input())
    if user_input >= 0:
        positives.append(user_input)
    else:
        negatives.append(user_input)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')