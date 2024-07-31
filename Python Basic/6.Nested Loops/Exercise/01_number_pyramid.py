n = int(input())

current_num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if current_num > n:
            break
        print(current_num, end=" ")
        current_num += 1
    print()