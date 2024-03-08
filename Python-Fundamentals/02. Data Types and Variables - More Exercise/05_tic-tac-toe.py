def check_winner(field):
    for row in field:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] != 0:
            return field[0][col]

    if field[0][0] == field[1][1] == field[2][2] != 0:
        return field[0][0]
    if field[0][2] == field[1][1] == field[2][0] != 0:
        return field[0][2]

    return 0


field = []
for _ in range(3):
    row = list(map(int, input().split()))
    field.append(row)

winner = check_winner(field)

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
