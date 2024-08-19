# rows, columns = map(int, input().split(", "))
#
# matrix = []
# for _ in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# for j in range(columns):
#     column_sum = sum(matrix[i][j] for i in range(rows))
#     print(column_sum)


data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    sum_col_nums = 0
    for row_index in range(rows):
        sum_col_nums += matrix[row_index][col_index]
    print(sum_col_nums)
