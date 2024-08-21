# rows, columns = map(int, input().split())
#
# matrix = []
# for _ in range(rows):
#     row = input().split()
#     matrix.append(row)
#
# def is_identical_square(i, j):
#     return matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]
#
# count = 0
# for i in range(rows - 1):
#     for j in range(columns - 1):
#         if is_identical_square(i, j):
#             count += 1
#
# print(count)

rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

count = 0

for row in range(rows-1):
    for col in range(columns-1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            count += 1
print(count)



