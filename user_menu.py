


class UserSystem:
    def __init__(self, library_name):
        self.library = Library(library_name)

    def display(self):
        print("Welcome to {self.library.name} Library\U0001F60D\n--------------------")
        user_entry = int(input("Press 1 to continue "))
        while user_entry != 1:
            user_entry = int(input("Sorry that's not a valid choice! Press 1 to continue"))
        print("Thank you for entering the Library system!\nPlease see the following options")
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Return Book"
              "\n5. List Available Books\n6. Search Book\n7. Save & Exit")
        user_input = int(input("Please enter a number from the options above \U0001F60D "))
        match user_input:
          case 1:
            book = Book()
            Library.add_book(book)
          case 2:
            user = User()
            Library.add_user(user)
          case 3:
            user_id = int(input("Please enter user id"))
            book_isbn = int(input("Please enter book isbn"))
            if Library.borrow_book(user_id, book_isbn):
                print("Book is available. Remember to return")
            else:
                print("Error: Book not found/Book is unavailable")
          case 4:
            user_id = int(input("Please enter user id"))
            book_isbn = int(input("Please enter book isbn"))
            if Library.return_book(user_id, book_isbn):
                print("Thank you for returning!")
            else:
                print("Error: Book not found/Book is already in Library")
          case 5:
            print("List of all Books available:")
            list_of_books = Library.list_available_books()
            counter = 1
            for book in list_of_books:
                print(f"{counter}: book.title")
                counter += 1
          case 6:
            title_or_author = input("Please enter the title or name of the author"
                                    " of the book you are searching for")
            if search_book(title_or_author):
                print("Book found!")
            else:
                print("Book not found!")
          case 7:
            print("Needs to EXIT here!!")
UserMenu.display(1)
