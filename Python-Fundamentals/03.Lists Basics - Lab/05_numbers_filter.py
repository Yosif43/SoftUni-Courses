lines = int(input())
numbers = []
filtered = []
for line in range(lines):
    user_input = int(input())
    numbers.append(user_input)

filter_cmd = input()
for number in numbers:
    if filter_cmd == "even":
        if number % 2 == 0:
            filtered.append(number)
    elif filter_cmd == "odd":
        if number % 2 == 1:
            filtered.append(number)
    elif filter_cmd == "negative":
        if number < 0:
            filtered.append(number)
    elif filter_cmd == "positive":
        if number >= 0:
            filtered.append(number)

print(filtered)