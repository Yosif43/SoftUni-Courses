from math import log

number = int(input())
command = input()

if command == "natural":
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, int(command)):.2f}")
