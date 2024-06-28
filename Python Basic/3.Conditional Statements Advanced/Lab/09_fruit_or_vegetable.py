my_input = input()
result = ""

if my_input == "banana" or my_input == "apple" or my_input == "kiwi" or my_input == "cherry" \
    or my_input == "lemon" or my_input == "grapes":
    result = "fruit"
elif my_input == "tomato" or my_input == "cucumber" or my_input == "pepper" or my_input == "carrot":
    result = "vegetable"
else:
    result = "unknown"
print(result)
