n = int(input())

my_stack = []

for _ in range(n):
    query = input().split()
    if query[0] == "1":
        my_stack.append(int(query[1]))
    elif my_stack:
        if query[0] == "2":
            my_stack.pop()
        elif query[0] == "3":
            print(max(my_stack))
        elif query[0] == "4":
            print(min(my_stack))

while my_stack:
    print(my_stack.pop(), end="")
    if my_stack:
        print(", ", end="")
