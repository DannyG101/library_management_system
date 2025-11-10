from modules.book import Book
from modules.user import User

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self,book:"Book"):
        self.books[book.isbn] = book

    def add_user(self,user:"User"):
        self.users[user.id] = user

    def borrow_book(self,user_id, book_isbn):
        if user_id in self.users and book_isbn in self.books:
            self.users[user_id].update_borrowed_books = self.books[book_isbn]
            self.books[book_isbn].update_book_status = False
            return True
        return False

    def return_book(self,user_id, book_isbn):
        if user_id in self.users and book_isbn in self.books:
            self.users[user_id].remove_borrowed_books(self.books[book_isbn])
            return True
        return False

    def list_available_books(self):
        list_books =  []
        for book in self.books:
            if book.update_book_status:
                list_books.append(book)
        return list_books

    def search_book(self,title_or_author):
        for book in self.books:
            if self.books[book].title == title_or_author or self.books[book].author == title_or_author:
                return True
        return False


