rows = int(input())
matrix = []

for row_index in range(rows):
    elements = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(elements)
print(matrix)


# rows = int(input())
# matrix = []
#
# for row_index in range(rows):
#     elements = [int(el) for el in input().split(", ")]
#     matrix.append(elements)
#
# even_matrix = []
#
# for row_index in range(rows):
#     even_matrix.append([])
#     for col_index in range(len(matrix[row_index])):
#         current_element = matrix[row_index][col_index]
#         if matrix[row_index][col_index] % 2 == 0:
#             even_matrix[row_index].append(current_element)
#
#
# print(even_matrix)
#
