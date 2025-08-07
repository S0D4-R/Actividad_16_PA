class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    def book_display(self):
        print(f"Libro: {self.name}|Autor: {self.author}|Año de publicación: {self.year}")