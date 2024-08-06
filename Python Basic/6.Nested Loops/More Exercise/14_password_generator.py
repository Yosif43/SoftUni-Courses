n = int(input().strip())
l = int(input().strip())

passwords = []

for digit1 in range(1, n + 1):
    for digit2 in range(1, n + 1):
        for char1 in range(ord('a'), ord('a') + l):
            for char2 in range(ord('a'), ord('a') + l):
                for digit3 in range(1, n + 1):
                    if digit3 > digit1 and digit3 > digit2:
                        password = f"{digit1}{digit2}{chr(char1)}{chr(char2)}{digit3}"
                        passwords.append(password)

print(' '.join(passwords))
