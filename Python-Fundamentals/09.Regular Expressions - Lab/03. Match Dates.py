import re

text = input()

patern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
matches = re.findall(patern, text)

for match in matches:
    separator = match[1]
    month = match[2]
    day = match[0]
    year = match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')
