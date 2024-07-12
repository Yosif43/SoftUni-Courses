n = int(input())

max_number = 0
min_number = 0

for i in range(n):
    user_input = int(input())
    if i == 0:
        min_number = user_input
        max_number = user_input
    else:
        if user_input > max_number:
            max_number = user_input
        if user_input < min_number:
            min_number = user_input

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
