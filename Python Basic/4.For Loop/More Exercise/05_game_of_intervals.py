n = int(input())
result = 0
invalid_numbers = 0
numbers_in_range = [0, 0, 0, 0, 0]

for i in range(n):
    num = int(input())
    if num < 0 or num > 50:
        invalid_numbers += 1
        result /= 2
    elif 0 <= num <= 9:
        result += num * 0.2
        numbers_in_range[0] += 1
    elif 10 <= num <= 19:
        result += num * 0.3
        numbers_in_range[1] += 1
    elif 20 <= num <= 29:
        result += num * 0.4
        numbers_in_range[2] += 1
    elif 30 <= num <= 39:
        result += 50
        numbers_in_range[3] += 1
    elif 40 <= num <= 50:
        result += 100
        numbers_in_range[4] += 1

percentages = [f"{100 * num / n:.2f}%" for num in numbers_in_range]
percentages.append(f"{100 * invalid_numbers / n:.2f}%")

print(f"{result:.2f}")
print(f"From 0 to 9: {percentages[0]}")
print(f"From 10 to 19: {percentages[1]}")
print(f"From 20 to 29: {percentages[2]}")
print(f"From 30 to 39: {percentages[3]}")
print(f"From 40 to 50: {percentages[4]}")
print(f"Invalid numbers: {percentages[5]}")