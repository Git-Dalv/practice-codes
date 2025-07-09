from __future__ import annotations  # !  add_book(self, other: *Book* )

from abc import ABC, abstractmethod
from datetime import datetime


class Library:
    def __init__(self) -> None:
        self.lib: list[Book] = []

    def __add__(self, other: 'Library') -> 'Library':  # Type annotation
        new_lib = Library()
        new_lib.lib = self.lib + other.lib
        return new_lib

    def __str__(self):
        books = ""
        for book in self.lib:
            books += book.__str__() + "\n"
        return books

    def __len__(self):
        return len(self.lib)

    def delete_book(self, *, book_author=None, book_title=None):  # "*" Keyword-only arguments (lib.delete_book(
        # book_title="1984"))
        if book_author:
            self.lib = [book for book in self.lib if book.author != book_author]
        if book_title:
            self.lib = [book for book in self.lib if book.title != book_title]

    def add_book(self, other: Book) -> None:  # Type annotation
        self.lib.append(other)


class Book(ABC):
    def __init__(self, title, author, year, pages):
        self._title = None
        self.title = title  # Method!
        self._author = None
        self.author = author  # Method!
        self._year = None
        self.year = year  # Method!
        self._pages = None
        self.pages = pages  # Method!

    @property  # <- @Decorator Getter
    def title(self):
        return self._title

    @title.setter  # <- ABS abstract method
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string!")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Author must be a string!")
        self._author = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("Year must be a integer!")
        self._year = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Pages must be a integer!")
        self._pages = value

    def is_old(self):
        return (datetime.now().year - self.year) > 50

    def __str__(self):
        return f"title: {self.title} author: {self.author} year:{self.year} pages: {self.pages}"

    @abstractmethod
    def read_sample(self):
        pass


class EBook(Book):
    FORMATS = {"PDF", "DOC", "EPUB", "MOBI", "DOCX"}

    def __init__(self, title, author, year, pages, form):
        super().__init__(title, author, year, pages)
        self._form = None
        self.form = form

    @property
    def form(self):
        return self._form

    @form.setter  # @Decorator Setter
    def form(self, value):
        if value.upper() not in self.FORMATS:  # Validation example
            raise ValueError(f"Form must be a:{self.FORMATS}")
        self._form = value.upper()

    def __str__(self):
        return f"title: {self.title} author: {self.author} year:{self.year} pages: {self.pages}, format: {self.form}"

    def read_sample(self):  # < - Polymorphism example
        print("Reading sample...")


class PrintedBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year, pages)

    def __str__(self):
        return super().__str__()

    def is_old(self):
        return super().is_old()

    def read_sample(self):  # < - Polymorphism example
        print("Reading sample...")


b1 = EBook("1984", "George Orwell", 1949, 328, "PDF")
b2 = PrintedBook("Brave New World", "Aldous Huxley", 1932, 288)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

print(lib)
print(f"Total books: {len(lib)}")
print(b1.is_old())  # True

lib.delete_book(book_title="1984")  # Because "*" -> book_title =
print(lib)
