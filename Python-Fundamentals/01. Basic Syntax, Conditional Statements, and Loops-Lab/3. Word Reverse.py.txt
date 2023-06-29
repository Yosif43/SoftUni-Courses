user_input = input()
reversed_word = ""

for i in range(len(user_input) - 1, -1, -1):
    reversed_word += user_input[i]

print(reversed_word)