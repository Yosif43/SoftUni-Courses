string = input()
digit = ""
letters = ""
other = ""

for ch in string:
    if ch.isdigit():
        digit += ch
    elif ch.isalpha():
        letters += ch
    else:
        other += ch

print(digit)
print(letters)
print(other)
