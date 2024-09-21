rows, cols = [int(el) for el in input().split(" ")]

matrix = []
moves = 0
opponent_touched = 0
enemy_players = 0
player_position = None
direction_mapper = {"up": (-1, 0),
                    "down": (1, 0),
                    "left": (0, -1),
                    "right": (0, 1)}

for row in range(rows):
    row_data = list(input().split())
    if "B" in row_data:
        col = row_data.index("B")
        player_position = [row, col]
    enemy_players += row_data.count("P")
    matrix.append(row_data)


command = input()
while command != "Finish":
    current_row, current_col = player_position
    row_to_go, col_to_go = direction_mapper[command]
    next_row = row_to_go + current_row
    next_col = col_to_go + current_col
    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):
        if command != "Finish" and matrix[next_row][next_col] != "O":
            moves += 1
        if matrix[next_row][next_col] == "-":
            matrix[next_row][next_col] = "B"
            matrix[current_row][current_col] = "-"
        elif matrix[next_row][next_col] == "P":
            matrix[next_row][next_col] = "B"
            opponent_touched += 1
            matrix[current_row][current_col] = "-"
        elif matrix[next_row][next_col] == "O":
            command = input()
            continue
    else:
        next_row = current_row
        next_col = current_col

    if opponent_touched == 3:
        break

    player_position = [next_row, next_col]
    command = input()

print(f"Game over!")
print(f"Touched opponents: {opponent_touched} Moves made: {moves}")
