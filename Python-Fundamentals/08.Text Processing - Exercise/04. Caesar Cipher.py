initial_message = input()
encrypted_message = ""
for character in initial_message:
    encrypted_character = chr(ord(character) + 3)
    encrypted_message += encrypted_character
print(encrypted_message)
