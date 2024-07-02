number1 = int(input())
number2 = int(input())
operator = input()

if operator == '+' or operator == '-' or operator == '*':
    result = 0
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2

    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'

    print(f"{number1} {operator} {number2} = {result} - {type_number}")
elif operator == '/' and number2 != 0:
    print(f"{number1} / {number2} = {number1 / number2:.2f}")
elif operator == '%' and number2 != 0:
    print(f"{number1} % {number2} = {number1 % number2}")

if number2 == 0:
    print(f"Cannot divide {number1} by zero")
