rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")
        continue
    if command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")


