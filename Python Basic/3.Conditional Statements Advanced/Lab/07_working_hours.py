number = int(input())
day = input()


if 10 <= number and number <= 18 and day != "Sunday":
    result = "open"
else:
    result = "closed"

print(result)
