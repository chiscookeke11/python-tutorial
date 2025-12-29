# Base class
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self._year_published = year_published  # encapsulation (protected)

    def book_age(self):
        return 2025 - self._year_published

    def read(self):
        print(f"You are reading '{self.title}' by {self.author}")




# Inheritance
class EBook(Book):
    def __init__(self, title, author, year_published, file_size):
        super().__init__(title, author, year_published)
        self.file_size = file_size

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB)")




# using the classes
book1 = Book("Physics Today", "J.J Thompson", 2014)
ebook1 = EBook("Modern Chemistry", "Okeke Chinedu", 2020, 5)

print(book1.book_age())
book1.read()

ebook1.download()
ebook1.read()




# Polymorphism
class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

class Boat:
    def move(self):
        print("Sailing")


vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
