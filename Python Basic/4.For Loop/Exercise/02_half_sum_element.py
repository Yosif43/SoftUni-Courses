import sys

max_sum = -sys.maxsize
count_numbers = int(input())
sum_numbers = 0

for i in range(0, count_numbers):
    num = int(input())
    if num > max_sum:
        max_sum = num
    sum_numbers += num

sum_numbers = sum_numbers - max_sum

if max_sum == sum_numbers:
    print("Yes")
    print(f"Sum = {max_sum}")
else:
    print("No")
    print(f"Diff = {abs(max_sum - sum_numbers)}")
