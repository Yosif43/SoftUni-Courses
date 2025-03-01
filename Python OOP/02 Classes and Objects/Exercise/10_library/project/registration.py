from project.user import User
from project.library import Library

class Registration:
    def add_user(self, user: User, library: Library):
        if any(u.user_id == user.user_id for u in library.user_records):
            return f"User with id = {user.user_id} already registered in the library!"
        else:
            library.user_records.append(user)
            return f"User with id = {user.user_id} added to the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            library.rented_books.pop(user.username, None)
            return f"User {user.username} removed from the library records."
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    old_username = user.username
                    user.username = new_username
                    if old_username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(old_username)
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"



user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
print(registration.add_user(user, library))
registration.remove_user(user, library)
print(registration.remove_user(user, library))
registration.add_user(user, library)
print(registration.change_username(2, 'Igor', library))
print(registration.change_username(12, 'Peter', library))
print(registration.change_username(12, 'George', library))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
print(library.books_available)
print(library.rented_books)
print(user.books)
