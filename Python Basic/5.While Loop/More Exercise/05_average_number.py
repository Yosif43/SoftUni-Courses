n = int(input())
sum = 0
for i in range(n):
    number = int(input())
    sum += number
average = sum / n
print(f"{average:.2f}")