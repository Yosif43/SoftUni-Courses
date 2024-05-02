text = input()
final_text = ""
last_character = ""
for char in text:
    if char != last_character:
        final_text += char
        last_character = char

print(final_text)
