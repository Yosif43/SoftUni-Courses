string = input()
number = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(string, number)
print(result)