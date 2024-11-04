from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}
        self.rented_books: Dict[str, Dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available.get(author, []):
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        elif any(book_name in books for books in self.rented_books.values()):
            return f"The book \"{book_name}\" is already rented and will be available in {days_to_return} days!"
        else:
            return f"The book \"{book_name}\" is not available."

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            if book_name in self.rented_books.get(user.username, {}):
                self.rented_books[user.username].pop(book_name, None)
            if author not in self.books_available:
                self.books_available[author] = []
            self.books_available[author].append(book_name)
            return f"{book_name} successfully returned."
        else:
            return f"{user.username} doesn't have this book in his/her records!"
