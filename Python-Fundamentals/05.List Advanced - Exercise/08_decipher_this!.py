def decipher_message(message):
    words = message.split()
    deciphered_words = []

    for word in words:
        if len(word) > 2:
            first_letter = chr(int(word[:2]))
            deciphered_word = first_letter + word[-1] + word[2:-1] + word[1]
        else:
            deciphered_word = chr(int(word))

        deciphered_words.append(deciphered_word)

    deciphered_message = ' '.join(deciphered_words)
    return deciphered_message


# Example usage
secret_message = input()
deciphered_message = decipher_message(secret_message)
print(deciphered_message)
