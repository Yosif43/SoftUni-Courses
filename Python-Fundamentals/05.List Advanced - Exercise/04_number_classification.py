#numbers = input()
#numbers_list = [int(num) for num in numbers.split(", ")]
#
#positive = [num for num in numbers_list if num >= 0]
#negative = [num for num in numbers_list if num < 0]
#even = [num for num in numbers_list if num % 2 == 0]
#odd = [num for num in numbers_list if num % 2 != 0]
#
#print("Positive:", ", ".join(map(str, positive)))
#print("Negative:", ", ".join(map(str, negative)))
#print("Even:", ", ".join(map(str, even)))
#print("Odd:", ", ".join(map(str, odd)))

#numbers = input().split(", ")
#positive = [number for number in numbers if int(number) >= 0]
#negative = [number for number in numbers if int(number) <= 0]
#even = [number for number in numbers if int(number) % 2 == 0]
#odd = [number for number in numbers if int(number) % 2 != 0]
#
#print(f"Positive: {', '.join(positive)}")
#print(f"Negative: {', '.join(negative)}")
#print(f"Even: {', '.join(even)}")
#print(f"Odd: {', '.join(odd)}")


def positive_numbers(some_numbers: list) -> list:
    return [number for number in numbers if int(number) >= 0]
def negative_numbers(some_numbers: list) -> list:
    return [number for number in numbers if int(number) <= 0]
def even_numbers(some_numbers: list) -> list:
    return [number for number in numbers if int(number) % 2 == 0]
def odd_numbers(some_numbers: list) -> list:
    return [number for number in numbers if int(number) % 2 != 0]

numbers = input().split(", ")

print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")

