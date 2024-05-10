import re

names = input()

pattern = r"\b_(?P<name>[A-Za-z0-9]+)\b"
valid_names = re.finditer(pattern, names)

final = []
for name in valid_names:
    final.append(name["name"])

print(*final, sep=",")