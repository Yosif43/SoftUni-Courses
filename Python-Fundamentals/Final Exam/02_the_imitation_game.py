def decipher_enigma(message, instructions):
    decrypted_message = message

    for instruction in instructions:
        command, *args = instruction.split('|')

        if command == 'Move':
            num_letters = int(args[0])
            decrypted_message = decrypted_message[num_letters:] + decrypted_message[:num_letters]

        elif command == 'Insert':
            index = int(args[0])
            value = args[1]
            decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]

        elif command == 'ChangeAll':
            substring = args[0]
            replacement = args[1]
            decrypted_message = decrypted_message.replace(substring, replacement)

        elif command == 'Decode':
            break

    return decrypted_message


# Example usage
encrypted_message = input()
instructions = []
while True:
    command = input()
    if command == 'Decode':
        break
    instructions.append(command)

decrypted_message = decipher_enigma(encrypted_message, instructions)
print("The decrypted message is:", decrypted_message)
