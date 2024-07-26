n, o, c = 0, 0, 0
word = ""

while True:
    letter = input()
    if letter == "End":
        break
    if letter == "n" and n == 0:
        n += 1
    elif letter == "o" and o == 0:
        o += 1
    elif letter == "c" and c == 0:
        c += 1
    else:
        if letter.isalpha():
            word += letter
    if n == 1 and c == 1 and o == 1:
        print(word, end=" ")
        word = ""
        n, o, c = 0, 0, 0


