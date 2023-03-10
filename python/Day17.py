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

bookId = 0
bookLibrary = []


def no_book(func):
    def inner():
            with open('book_list.txt', 'r') as file:
                books = len(file.readlines()) // 5
            if books != 0:
                print('There are', books, 'books!\n')
            else:
                print('There is no book on the list')
            with open('book_list.txt', 'r') as file:
                print(file.read())
    return inner
with open('book_id.txt', 'r') as file:
    x = file.readlines()
    if len(x) != 0:
            book_id = x[0]
    else:
            book_id = 1


@no_book
def show_all():

    print(f'There are {bookId} books!')
    print("***********************")

def add_book():
    
    nameBook = input("Enter book name:")
    nameWriter = input("Enter writer name:")
    addedTime = datetime.datetime.today().strftime('%d %B %Y')
    print("Added Succesfully!")
    with open('book_list.txt', 'a') as file:
        file.write(
            f"Book ID: {book_id}\nBook name: {nameBook}\nWriter: {nameWriter}\nAdded in: {addedTime}\n***********************\n ")
    count = int(book_id) + 1
    with open('book_id.txt', 'w') as file:
        file.write(str(count))

def show_book():
    enteredBook = int(input('Enter book ID:\n'))
    with open('book_list.txt', 'r') as file:
        lines = file.readlines()
        if f'Book ID: {enteredBook}\n' in lines:
            index = lines.index(f'Book ID: {enteredBook}\n')
            k = 0
            while k < 4:
                print(lines[index])
                index += 1
                k += 1
        else:
            print("This book does not exist")

def remove_book():
    lines = []
    num = []
    enteredBook = int(input('Enter book ID:\n'))

    with open('book_list.txt', 'r') as file:

        lines = file.readlines()

        if f'Book ID: {enteredBook}\n' in lines:
            print("Deleted Succesfully!")
            index = lines.index(f'Book ID: {enteredBook}\n')
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

if 'add' in requ:
    

    add_book()

elif 'show' in requ and 'all' in requ:
    show_all()
    # with open('book_list.txt', 'r') as file:
    #     print(file.read())
elif 'show' in requ and 'book' in requ:
    show_book()
elif "remove" in requ:
    remove_book()
    bookId -= 1
else:
    print("Wrong input")
