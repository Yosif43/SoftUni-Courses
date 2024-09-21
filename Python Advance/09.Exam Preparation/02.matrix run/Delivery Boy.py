ROW, COL = [int(el) for el in input().split()]

matrix = [list(input()) for _ in range(ROW)]


boy_row, boy_col = None, None
for row in range(ROW):

    for col in range(COL):
        if matrix[row][col] == 'B':
            boy_row, boy_col = row, col

commands = []
command = input()
while command:
    commands.append(command)
    command = input()


pizza_collected = False
delivery_successful = False

for command in commands:
    new_row, new_col = boy_row, boy_col

    if command == "up":
        new_row -= 1
    elif command == "down":
        new_row += 1
    elif command == "left":
        new_col -= 1
    elif command == "right":
        new_col += 1

    if 0 <= new_row < ROW and 0 <= new_col < COL:
        if matrix[new_row][new_col] == '-' or matrix[new_row][new_col] == "R":
            if matrix[new_row][new_col] == "R":
                continue
            matrix[boy_row][boy_col] = '.'
            boy_row, boy_col = new_row, new_col
            matrix[boy_row][boy_col] = 'B'
        elif matrix[new_row][new_col] == 'A':
            matrix[new_row][new_col] = 'P'
            delivery_successful = True
            break
        elif matrix[new_row][new_col] == 'P':
            matrix[new_row][new_col] = 'R'
            matrix[boy_row][boy_col] = '.'
            boy_row, boy_col = new_row, new_col
            matrix[boy_row][boy_col] = 'B'
            pizza_collected = True
    else:
        break

if delivery_successful:
    print("Pizza is delivered on time! Next order...")
elif pizza_collected:
    print("Pizza is collected. 10 minutes for delivery.")
else:
    print("The delivery is late. Order is canceled.")

for row in matrix:
    print("".join(row))

