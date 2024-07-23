looking_book_name = input()

books_counter = 0
book_name = input()
is_book_found = False

while book_name != "No More Books":
    if looking_book_name == book_name:
        is_book_found = True
        break

    books_counter += 1
    book_name = input()

if is_book_found:
    print(f"You checked {books_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_counter} books.")
