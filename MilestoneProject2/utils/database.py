def books():
    with open('books.txt','r') as f:
        books = f.readlines()
        return books

def addBooks(name, author):
    book = books()
    book.append({'name': name, 'author': author, 'read': False})
    with open('books.txt', 'w') as f:
        f.write(f'{book}')

def showList():
    book = books()
    print(book)

def delete():
    book = str(books())
    book.strip().split('[','\')
    print(book)
delete()