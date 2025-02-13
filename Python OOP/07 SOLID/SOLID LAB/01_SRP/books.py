from typing import List, Optional


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str) -> Optional[Book]:
        try:
            book = [b for b in self.books if b.title.lower() == title.lower()][0]
            return book
        except IndexError:
            return None


book = Book("Title1", "test")
book2 = Book("Title2", "Test2")

library = Library()
print(library.books)
library.add_book(book)
print(library.books)
print(library.find_book("ASd"))
print(library.find_book("title1"))
