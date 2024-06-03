'''
SOLID Design Principles
The 5 that represent SOLID are the most crucial ones a software developer should know.

Single Responsibility principle
    A class should have one responsibility and no more
'''

class Books():
    '''
    Represents a collection of books.
    '''

    def __init__(self):
        '''
        Initializes an instance of the Books class.
        '''
        self.books = {}
        self.number = 0

    def add_book(self, book):
        '''
        Adds a book to the collection.

        Parameters:
            book (str): The name of the book to add.
        '''
        self.number += 1
        self.books[self.number] = book

    def str_(self):
        '''
        Returns a string representation of the books collection.

        Returns:
            str: The string representation of the books collection.
        '''
        return str(self.books)

    ## Violets the Single responsibility principle Create seperate class
    def store_books(self, filename):
        '''
        Stores the books collection in a file.

        Parameters:
            filename (str): The name of the file to store the books collection in.
        '''
        with open(filename, 'w') as f:
            f.write(str(self.books))


class StoreBooks():
    '''
    Represents a class for storing books in a file.
    '''

    def save_books(self, filename, books): 
        '''
        Saves the books collection in a file.

        Parameters:
            filename (str): The name of the file to save the books collection in.
            books (dict): The books collection to save.
        '''
        with open(filename, 'w') as f:
            f.write(str(books))


a = Books()
a.add_book('Book A')
a.add_book('Book B')
print(f"The books I have read are: {a}")
a.store_books('filename.txt')

b = StoreBooks()
b.save_books('filename1.txt', a.books)
