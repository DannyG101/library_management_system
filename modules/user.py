


class User:
    def __init__(self, name:str, id:int, borrowed_books:list["Book"]=[]):
        self.name = name
        self.id = id
        self.__borrowed_books = borrowed_books

    def __str__(self):
        return f"User name: {self.name}, User id: {self.id}, Borrowed books: {self.__borrowed_books}"