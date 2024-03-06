number = int(input())
is_prime = True

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
print(is_prime)