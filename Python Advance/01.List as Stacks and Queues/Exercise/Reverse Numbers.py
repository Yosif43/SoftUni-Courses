# numbers = input().split()
#
# while numbers:
#     print(numbers.pop(), end=" ")

numbers = [x for x in input().split()]
stack = []

while numbers:
    stack.append(numbers.pop())

print(" ".join(stack))
    