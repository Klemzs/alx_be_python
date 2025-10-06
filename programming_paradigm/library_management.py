class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return
        return f"{title} is available"

    def return_book(self,title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return
        return f"'{title}' was not checked out."

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            for title in available_books:
                print(f"- {title}")
        else:
            print("No books available.")
