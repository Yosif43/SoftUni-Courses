smallest_number = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    user_input = int(user_input)
    if user_input < smallest_number:
        smallest_number = user_input

print(smallest_number)
