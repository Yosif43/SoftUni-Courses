size = int(input())
matrix = [list(input()) for _ in range(size)]

position = (0, 0)
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'S':
            position = (row, col)

fish_caught = 0
while True:
    command = input()
    if command == "collect the nets":
        break

    current_row, current_col = position
    new_position = position

    if command == "up":
        new_position = ((current_row - 1) % size, current_col)
    elif command == "down":
        new_position = ((current_row + 1) % size, current_col)
    elif command == "left":
        new_position = (current_row, (current_col - 1) % size)
    elif command == "right":
        new_position = (current_row, (current_col + 1) % size)

    if matrix[new_position[0]][new_position[1]] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{new_position[0]},{new_position[1]}]")
        exit()
    elif matrix[new_position[0]][new_position[1]].isdigit():
        fish_caught += int(matrix[new_position[0]][new_position[1]])
        matrix[new_position[0]][new_position[1]] = 'S'
    else:
        matrix[new_position[0]][new_position[1]] = 'S'

    matrix[current_row][current_col] = '-'
    position = new_position

if fish_caught >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_caught} tons of fish more.")

if fish_caught > 0:
    print(f"Amount of fish caught: {fish_caught} tons.")

for row in matrix:
    print(''.join(row))
