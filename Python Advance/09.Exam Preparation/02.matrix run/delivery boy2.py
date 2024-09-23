rows, cols = [int(x) for x in input().split()]


def check_valid_index_area(row, col):
    return 0 <= row < rows and 0 <= col < cols


matrix = []
delivery_boy_position = None

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for row_index in range(rows):
    row_data = list(input())
    if "B" in row_data:
        col_index = row_data.index("B")
        delivery_boy_position = [row_index, col_index]
    matrix.append(row_data)
initial_row, initial_col = delivery_boy_position
direction = input()

while direction:
    current_row, current_col = delivery_boy_position
    row_to_go, col_to_go = direction_mapper[direction]
    desire_row = row_to_go + current_row
    desire_col = current_col + col_to_go

    if not check_valid_index_area(desire_row, desire_col):
        print("The delivery is late. Order is canceled.")
        matrix[initial_row][initial_col] = " "
        break

    elif matrix[desire_row][desire_col] == "*":
        direction = input()
        continue
    elif matrix[desire_row][desire_col] == "P":
        matrix[desire_row][desire_col] = "R"
        matrix[current_row][current_col] = "."
        print("Pizza is collected. 10 minutes for delivery.")
    elif matrix[desire_row][desire_col] == "A":
        matrix[desire_row][desire_col] = "P"
        matrix[current_row][current_col] = "."
        print("Pizza is delivered on time! Next order...")
        break
    elif matrix[desire_row][desire_col] == "-":
        if not matrix[current_row][current_col] == "R":
            matrix[desire_row][desire_col] = "."
        else:
            matrix[desire_row][desire_col] = "."

    delivery_boy_position = [desire_row, desire_col]
    direction = input()

for row in matrix:
    print(*row, sep="")