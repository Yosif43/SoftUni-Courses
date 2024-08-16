first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + " " + line[1]
    numbers = [int(num) for num in line[2:]]
    if command == "Add First":
        first_set.update(numbers)
    if command == "Add Second":
        second_set.update(numbers)
    if command == "Remove First":
        first_set.difference_update(numbers)
    if command == "Remove Second":
        second_set.difference_update(numbers)
    if command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

