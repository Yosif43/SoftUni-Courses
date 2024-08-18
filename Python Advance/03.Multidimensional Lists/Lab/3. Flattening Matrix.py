# rows = int(input())
# matrix = []
# united_matrix = []
# for row in range(rows):
#     elements = [int(el) for el in input().split(", ")]
#     matrix.append(elements)
#
# for r in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         united_matrix.append(matrix[r][col])
#
# print(united_matrix)


rows = int(input())
matrix = []
for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

flattened = []

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattened.append(matrix[row_index][col_index])

print(flattened)

flattened = []

for row in matrix:
    for el in row:
        flattened.append(el)
print([el for row in matrix for el in row])
print(flattened)