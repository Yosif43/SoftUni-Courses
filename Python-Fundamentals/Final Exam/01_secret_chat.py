concealed = input()
command = input()


def insert_space(index, main_string):
    return main_string[:index] + " " + main_string[index:]


def reverse_(substring, main_string):
    word_find = main_string.find(substring)
    main_string = main_string[:word_find] + main_string[word_find + len(substring):]
    main_string += substring[::-1]
    return main_string


def change_all(substring, replacement, main_string):
    return main_string.replace(substring, replacement)


while command != "Reveal":
    command_type, *info = command.split(":|:")
    found_error = False

    if command_type == "ChangeAll":
        substring, replacement = info
        concealed = change_all(substring, replacement, concealed)
    else:
        if command_type == "Reverse":
            substring = info[0]
            if substring not in concealed:
                print("error")
                found_error = True
            else:
                concealed = reverse_(substring, concealed)
        elif command_type == "InsertSpace":
            index_ = int(info[0])
            concealed = insert_space(index_, concealed)

    if not found_error:
        print(concealed)

    command = input()

print(f"You have a new text message: {concealed}")