strings = input().split("|")
matrix = []

for i in range(len(strings) - 1, -1, -1):
    row = [int(x) for x in strings[i].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, sep=" ", end=" ")

