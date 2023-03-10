import datetime
import os
import sys
requ = sys.argv
os.chdir('bse-bookshop-project-Cavid370')
if not os.path.exists('books'):
    os.mkdir('books')
os.chdir('books')
if not os.path.exists('book_list.txt'):
    open('book_list.txt', 'w').close()

if not os.path.exists('book_id.txt'):
    open('book_id.txt', 'w').close()
class Books:
    def set_id(self):
        with open('book_id.txt', 'r') as file:
            x = file.readlines()
        if len(x) != 0:
            book_id = x[0]
        else:
            book_id = 1
        return book_id
    def set_date(self):
        date = datetime.datetime.today().strftime('%d %B %Y')
        return date
    def show_all(self,books):
        if books != 0:
                print('There are', books, 'books!\n')
                with open('book_list.txt', 'r') as file:
                    print(file.read())
        else:
            print('There is no book on the book list')

    def show_book(self,show_id):
        with open('book_list.txt', 'r') as file:
            lines = file.readlines()
            if f'Book ID: {show_id}\n' in lines:
                index = lines.index(f'Book ID: {show_id}\n')
                k = 0
                while k < 4:
                    print(lines[index])
                    index += 1
                    k += 1
            else:
                print("This book does not exist")

    def add_book(self,title,author):
        with open('book_list.txt', 'a') as file:
            file.write(f"Book ID: {self.set_id()}\nBook name: {title}\nWriter: {author}\nAdded in: {self.set_date()}\n***********************\n")
        count = int(self.set_id()) + 1
        with open('book_id.txt', 'w') as file:
            file.write(str(count))

    def remove_book(self,remove_id):
        lines = []
        num = []

        with open('book_list.txt', 'r') as file:

            lines = file.readlines()

            if f'Book ID: {remove_id}\n' in lines:
                print("Deleted Succesfully!")
                index = lines.index(f'Book ID: {remove_id}\n')
                k = 0
                while k < 5:
                    num.append(index)
                    index += 1
                    k += 1
                with open('book_list.txt', 'w') as file:
                    for number, line in enumerate(lines):
                        if number not in num:
                            file.write(line)
            else:
                print("Bu İD-də kitab yoxdur")
book=Books()
if 'add' in requ:
    title = input('Enter book name:\n')
    author = input('\nEnter writer name:\n')
    print('\nAdded succesfully!')
    book.add_book(title,author)


elif 'show' in requ and 'all' in requ:
    with open('book_list.txt', 'r') as file:
        # print(file.read())
        books = len(file.readlines()) // 5
    book.show_all(books)

elif 'show' in requ and 'book' in requ:
    show_id = int(input('Enter book ID:\n'))
    book.show_book(show_id)
elif "remove" in requ:
    remove_id = int(input('Enter book ID:\n'))
    book.remove_book(remove_id)
    
else:
    print("Wrong input")