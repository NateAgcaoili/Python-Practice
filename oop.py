### Object Oriented Programming in Python ###
class Book():
    
    favorites = [] #class level list variable
    
    def __init__(self, title, pages): #python constructor
        self.title = title
        self.pages = pages
    
    def __str__(self): #string representation of book objects
        return f"{self.title} is {self.pages} pages long."
    
    def __eq__(self, other): #comparing two book objects
        if self.title == other.title and self.pages == other.pages:
            return True
        return False

    def is_long(self): 
        if self.pages > 100:
            return True
        return False

    __hash__ = None #book is mutable, so don't hash

### Practice ###
book1 = Book("The Three Little Pigs", 72)
print(book1.title)
print(book1.is_long)
print(book1)

book2 = Book("The Three Little Pigs", 72)
book3 = Book("The Bible", 420)
book4 = book1
print(book1 == book2)
print(book1 == book3)
print(book1 is book4) #checking if they are equal in memory
print(book1 is book2)

def title_changer(book, title): 
    book.title = title
    book = Book(title,100) #pass by reference, this will not change the original object

title_changer(book1, "New Title!")
print(book1)

### File I/O ###
file = open("input.txt", 'w') #writing books to file
file.write("Harry Potter\t230") 
file.write("\nFairy Tales\t150")
file.close()

try:
    file = open("input.txt", 'r')
    data = file.read().split('\n') #splitting books from file up
    file.close()
    
    print(data)

    book5_data =  data[0].split('\t') #creating new book based off data from file
    book5 = Book(book5_data[0], book5_data[1])
    print(book5)
except FileNotFoundError as e:
    print("Could not open file")
except Exception as e:
    print("Something went wrong")
finally:
    file.close()
    print("done")

try:
    file = open("input.txt", 'r')
except OSError:
    print("Cannot Open")
else:
    with file:
        data = file.read().split('\n')
        book6_data = data[1].split('\t')
        book6 = Book(book6_data[0], book6_data[1])
        print(book6)
