# matrix = []
#
# data = input().split(", ")
# rows = int(data[0])
# cols = int(data[1])
#
# for row in range(rows):
#     elements = [int(el) for el in input().split(", ")]
#     matrix.append(elements)
#
# sum_nums = 0
#
# for row_index in range(rows):
#     for col_index in range(cols):
#         sum_nums += matrix[row_index][col_index]
# print(sum_nums)
# print(matrix)

matrix = []

data = input().split(", ")
rows = int(data[0])
cols = int(data[1])
sum_nums = 0

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    sum_nums += sum(elements)
    matrix.append(elements)

print(sum_nums)
print(matrix)
# Less code speed