n = int(input())
unique = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        unique.add(el)

for result in unique:
    print(result)