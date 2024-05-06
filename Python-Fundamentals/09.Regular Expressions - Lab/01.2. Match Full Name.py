import re
names = input()

valid_names = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)
print(*valid_names, sep=" ")