divisor = int(input())
boundary = int(input())
highest_integer = 0

for num in range(1, boundary + 1):
    if num % divisor == 0:
        if num > highest_integer:
            highest_integer = num

print(highest_integer)