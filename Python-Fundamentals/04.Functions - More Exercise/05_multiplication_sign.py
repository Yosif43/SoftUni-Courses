def multiplication_sign(a, b, c):
    negative_count = sum(1 for x in [a, b, c] if x < 0)

    if 0 in [a, b, c]:
        return "zero"
    elif negative_count % 2 == 1:
        return "negative"
    else:
        return "positive"

a = int(input())
b = int(input())
c = int(input())

print(multiplication_sign(a, b, c))

