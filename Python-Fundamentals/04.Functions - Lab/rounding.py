given_numbers = list(map(float, input().split(" ")))
rounded_numbers = []

for number in given_numbers:
    rounded_numbers.append(round(number))


print(rounded_numbers)