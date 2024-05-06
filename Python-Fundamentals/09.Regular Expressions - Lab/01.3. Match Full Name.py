import re
names = input()

valid_names = re.finditer(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)

for name in valid_names:
    print(name.group(), end=" ")