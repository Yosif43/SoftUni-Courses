def print_groups(numbers):
    numbers = [int(num) for num in numbers.split(",")]
    group = 10

    while numbers:
        group_numbers = [num for num in numbers if num <= group]
        if group_numbers:
            print(f"Group of {group}'s: {group_numbers}")
        else:
            print(f"Group of {group}'s: {group_numbers}")

        numbers = [num for num in numbers if num > group]
        group += 10

numbers = input()
print_groups(numbers)
