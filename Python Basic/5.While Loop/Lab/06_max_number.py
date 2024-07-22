biggest_number = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    user_input = int(user_input)
    if user_input > biggest_number:
        biggest_number = user_input

print(biggest_number)
