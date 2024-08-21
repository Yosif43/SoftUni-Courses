rows = int(input())

matrix = [[int(el) for el in input().split(", ")]for row in range(rows)]
# for row in range(rows):
#     elements = [int(el) for el in input().split(", ")]
#     matrix.append(elements)
primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")



