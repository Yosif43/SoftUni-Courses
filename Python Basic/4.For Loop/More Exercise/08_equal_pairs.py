import sys

n = int(input())
maxdiff = -sys.maxsize

for i in range(n):
    number1 = int(input())
    number2 = int(input())
    value = number1 + number2
    if i % 2 == 0:
        sum1 = value
    else:
        sum2 = value
    if i != 0:
        diff = abs(sum1 - sum2)
        if diff > maxdiff:
            maxdiff = diff
    else:
        maxdiff = 0

if maxdiff == 0:
    print(f"Yes, value={value}")
else:
    print(f"No, maxdiff={maxdiff}")
