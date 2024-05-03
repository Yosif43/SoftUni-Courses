import re

def calculate_string(string):
    result = 0

    parts = re.findall(r'(\d+|[A-Za-z])', string)

    for i in range(len(parts)):
        part = parts[i]

        if part.isdigit():
            number = int(part)

            if i > 0 and parts[i - 1].isalpha():
                prev_letter = parts[i - 1]

                if prev_letter.isupper():
                    position = ord(prev_letter) - ord('A') + 1
                    number /= position
                elif prev_letter.islower():
                    position = ord(prev_letter) - ord('a') + 1
                    number *= position

            if i < len(parts) - 1 and parts[i + 1].isalpha():
                next_letter = parts[i + 1]

                if next_letter.isupper():
                    position = ord(next_letter) - ord('A') + 1
                    number -= position
                elif next_letter.islower():
                    position = ord(next_letter) - ord('a') + 1
                    number += position

            result += number

    return result
input_data = input().split()
total_sum = sum(calculate_string(string) for string in input_data)
print(f'{total_sum:.2f}')