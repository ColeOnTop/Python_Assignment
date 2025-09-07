# Assignment 1: Book Class with Inheritance 

class Book:
    def _init_(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def read(self):
        print(f"You start reading '{self.title}' by {self.author}. 📖")

    def info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages - Genre: {self.genre}"


# Inheritance: EBook is a type of Book
class EBook(Book):
    def _init_(self, title, author, pages, genre, file_size):
        super()._init_(title, author, pages, genre)
        self.file_size = file_size  # extra attribute

    def read(self):
        print(f"You are reading '{self.title}' on your e-reader. 💻 (Size: {self.file_size}MB)")


class AudioBook(Book):
    def _init_(self, title, author, pages, genre, narrator):
        super()._init_(title, author, pages, genre)
        self.narrator = narrator  # extra attribute

    def read(self):
        print(f"Listening to '{self.title}' narrated by {self.narrator}. 🎧")

# Activity 2: Polymorphism Challenge 
def start_reading(book):
    book.read()


# Create objects
physical_book = Book("The Hobbit", "J.R.R. Tolkien", 310, "Fantasy")
ebook = EBook("1984", "George Orwell", 328, "Dystopian", 2.5)
audiobook = AudioBook("Becoming", "Michelle Obama", 400, "Memoir", "Michelle Obama")

# Display info
print(physical_book.info())
print(ebook.info())
print(audiobook.info())

# Polymorphism in action
start_reading(physical_book)  # Book version
start_reading(ebook)          # EBook version
start_reading(audiobook)      # AudioBook version
