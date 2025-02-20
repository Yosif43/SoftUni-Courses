def fibonacci():
    curr_num, next_num = 0, 1
    while True:
        yield curr_num
        curr_num, next_num = next_num, curr_num + next_num

generator = fibonacci()
for i in range(5):
    print(next(generator))
print()
generator = fibonacci()
for i in range(1):
    print(next(generator))