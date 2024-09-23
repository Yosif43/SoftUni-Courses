size = int(input())

matrix = []
lives = 3
enemy_ships_destroyed = 0

direction_mapper = {"up": (-1, 0),
                    "down": (1, 0),
                    "left": (0, -1),
                    "right": (0, 1)}
submarine_position = None

for row in range(size):
    row_data = (list(input()))
    if "S" in row_data:
        col_index = row_data.index("S")
        submarine_position = [row, col_index]
    matrix.append(row_data)
initial_row, initial_col = submarine_position


direction = input()
while direction:
    current_row, current_col = submarine_position
    row_to_go, col_to_go = direction_mapper[direction]
    desire_row = row_to_go + current_row
    desire_col = col_to_go + current_col
    if matrix[desire_row][desire_col] == "-":
        matrix[desire_row][desire_col] = "S"
        matrix[current_row][current_col] = "-"
    elif matrix[desire_row][desire_col] == "*":
        matrix[desire_row][desire_col] = "S"
        matrix[current_row][current_col] = "-"
        lives -= 1
        if lives <= 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{desire_row}, {desire_col}]!")
            break
    elif matrix[desire_row][desire_col] == "C":
        matrix[desire_row][desire_col] = "S"
        matrix[current_row][current_col] = "-"
        enemy_ships_destroyed += 1
        if enemy_ships_destroyed == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    submarine_position = [desire_row, desire_col]
    direction = input()

for row in matrix:
    print(*row, sep="")
