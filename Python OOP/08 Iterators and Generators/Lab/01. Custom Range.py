class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            number = self.current
            self.current += 1
            return number

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
