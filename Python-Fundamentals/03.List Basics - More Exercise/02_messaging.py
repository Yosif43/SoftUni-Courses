numbers = input()
text = input()

def send_message(numbers, text):
    numbers_list = numbers.split()
    message = ""

    for num in numbers_list:
        index = sum(int(digit) for digit in num)
        while index >= len(text):
            index -= len(text)
        message += text[index]
        text = text[:index] + text[index+1:]

    print(message)
send_message(numbers, text)
