from functools import reduce

class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)
    #   return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result
    #   return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    #   return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    #   return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
