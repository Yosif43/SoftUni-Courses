def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

# Examples
print(list(squares(5)))


def squares(n):
    current = 1
    while current <= n:
        yield current * current
        current += 1

print(list(squares(5)))
