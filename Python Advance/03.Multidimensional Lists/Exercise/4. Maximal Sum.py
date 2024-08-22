# rows, columns = map(int, input().split())
#
# matrix = []
# for _ in range(rows):
#     matrix.append(list(map(int, input().split())))
#
# max_sum = float('-inf')
# top_left_row = 0
# top_left_col = 0
#
# for row in range(rows - 2):
#     for col in range(columns - 2):
#         current_sum = sum(matrix[row][col:col + 3]) + sum(matrix[row + 1][col:col + 3]) + sum(matrix[row + 2][col:col + 3])
#         if current_sum > max_sum:
#             max_sum = current_sum
#             top_left_row = row
#             top_left_col = col
# m
# print(f"Sum = {max_sum}")
#
# for i in range(top_left_row, top_left_row + 3):
#     print(" ".join(map(str, matrix[i][top_left_col:top_left_col + 3])))

rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float("-inf")
max_row = 0
max_col = 0

for row in range(rows-2):
    for col in range(columns-2):
        current_sum = 0
        # current_sum += matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
        #     matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {max_sum}")

max_submatrix = [matrix[r][max_col:max_col + 3]for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]


