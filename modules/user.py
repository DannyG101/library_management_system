


class User:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self.__borrowed_books = []
    def __str__(self):
        return f"User name: {self.name}, User id: {self.id}, Borrowed books: {self.__borrowed_books}"

    @property
    def update_borrowed_books(self):
        return self.__borrowed_books

    @update_borrowed_books.setter
    def update_borrowed_books(self, book):
        self.__borrowed_books.append(book)