

class Book:
    def __init__(self,title:str ,author:str ,isbn:int):
        self.__is_available:bool = True
        self.title = title
        self.author = author
        self.isbn = isbn

    def book_info(self):
        print(f"title:{self.title}, author:{self.author},"
        f" isbn:{self.isbn}, is_available: {self.__is_available}")

    @property
    def update_book_status(self):
        return self.__is_available

    @update_book_status.setter
    def update_book_status(self,new_status):
        self.__is_available = new_status


