list_numbers = input().strip().split(", ")

for i in range(0, len(list_numbers)):
    if list_numbers[i] == "0":
        list_numbers.remove("0")
        list_numbers.append("0")

list_numbers = [int(i) for i in list_numbers]
print(list_numbers)