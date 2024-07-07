"""
Let's create a simple program using Object-Oriented Programming (OOP) principles
in Python. We'll build a basic system for managing a library,
 where you can add books, view all books, and search for a book by title.

"""
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f"'{self.title}', by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

# Example usage:
book1 = Book("George Orwell", "1984")
library = Library()
library.add_book(book1)










