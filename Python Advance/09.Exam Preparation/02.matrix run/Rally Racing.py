def move_car(x, y, direction):
    if direction == "up":
        return x - 1, y
    elif direction == "down":
        return x + 1, y
    elif direction == "left":
        return x, y - 1
    elif direction == "right":
        return x, y + 1

def find_tunnel(matrix, x, y):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'T' and (i != x or j != y):
                return i, j
    return x, y

N = int(input())
racing_number = input()
matrix = [list(input().split()) for _ in range(N)]
x, y = 0, 0
distance = 0

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    x, y = move_car(x, y, command)
    if matrix[x][y] == 'F':
        distance += 10
        print(f"Racing car {racing_number} finished the stage!")
        break
    elif matrix[x][y] == 'T':
        matrix[x][y] = '.'
        x, y = find_tunnel(matrix, x, y)
        matrix[x][y] = '.'
        distance += 30
    else:
        distance += 10

print(f"Distance covered {distance} km.")
matrix[x][y] = 'C'
for row in matrix:
    print(''.join(row))
