from modules.book import Book
from modules.library import Library
from modules.user import User



class UserSystem:
    @staticmethod
    def login_to_the_system():
        print("Welcome to your Library\U0001F60D\n--------------------")
        user_entry = int(input("Press 1 to continue "))

        while user_entry != 1:
            user_entry = int(input("Sorry that's not a valid choice! Press 1 to continue"))
        print("Thank you for entering the Library system!\nPlease see the following options")
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Return Book"
              "\n5. List Available Books\n6. Search Book\n7. Save & Exit")


    @staticmethod
    def central_user_system():
        my_library = Library()
        user_exit = False
        while not user_exit:
            user_input = int(input("Please enter a number from the options above \U0001F60D "))

            match user_input:
              case 1:
                title = input("Please enter the book title ")
                author = input("Please enter the book author ")
                isbn = int(input("Please enter the book isbn "))
                book = Book(title, author, isbn)
                my_library.add_book(book)

              case 2:
                name = input("Please enter user name ")
                user_id = int(input("PLease enter id "))
                user = User(name, user_id)
                my_library.add_user(user)

              case 3:
                user_id = int(input("Please enter user id "))
                book_isbn = int(input("Please enter book isbn "))
                if my_library.borrow_book(user_id, book_isbn):
                    print("Book is available. Remember to return")
                else:
                    print("Error: Book not found/Book is unavailable")

              case 4:
                user_id = int(input("Please enter user id"))
                book_isbn = int(input("Please enter book isbn"))
                if my_library.return_book(user_id, book_isbn):
                    print("Thank you for returning!")
                else:
                    print("Error: Book not found/Book is already in Library")

              case 5:
                print("List of all Books available:")
                list_of_books = my_library.list_available_books()
                counter = 1
                for book in list_of_books:
                    print(f"{counter}: {book}")
                    counter += 1

              case 6:
                title_or_author = input("Please enter the title or name of the author"
                                        " of the book you are searching for")
                if my_library.search_book(title_or_author):
                    print("Book found!")
                else:
                    print("Book not found!")

              case 7:
                  print("Thanks for visiting Library")
                  user_exit = True

