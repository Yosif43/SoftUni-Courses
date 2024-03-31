def process_data(data_type):
    if data_type == 'int':
        number = int(input())
        result = number * 2
        print(result)
    elif data_type == 'real':
        number = float(input())
        result = format(number * 1.5, '.2f')
        print(result)
    elif data_type == 'string':
        string = input()
        result = f"${string}$"
        print(result)

data_type = input()
process_data(data_type)