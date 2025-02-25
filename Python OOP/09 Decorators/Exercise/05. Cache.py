def cache(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.log[args[0]] = result
        return result
    wrapper.log = {}
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)
print()
fibonacci(4)
print(fibonacci.log)