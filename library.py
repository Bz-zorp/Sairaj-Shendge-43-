class Book:
    def __init__(self, book_id, title, author, quantity=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity  # Track available copies

    def check_availability(self):
        return self.quantity > 0

    def update_quantity(self, amount):
        self.quantity += amount

    def display_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_quantity(1)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        if any(u.user_id == user.user_id for u in self.users):
            print("User ID already exists.")
            return
        self.users.append(user)

    def search_book(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]
