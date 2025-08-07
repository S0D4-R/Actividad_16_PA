books_compendium = []

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    def book_display(self):
        print(f"Libro: {self.name}|Autor: {self.author}|Año de publicación: {self.year}")


def add_book(compendium):
    nombre = input("\nColoque el nombre del libro: ")
    autor = input("Coloque el nombre del autor: ")
    year_conf = False
    while not year_conf:
        try:
            yr = int(input("Coloque el año de publicación: "))
            if yr < 0:
                print("Año no válido")
            else:
                year_conf = True
        except ValueError:
            print("Eso no es un número")
    compendium.append(Book(nombre,autor,yr))
key = True
while key:
    try:
        print("----------Menú-----------")
        ops = input("1.Agregar libros\n"
                    "2.Mostrar la lista de libros\n"
                    "3.Eliminar libros por título\n"
                    "4.Salir del programa.\n"
                    "Opción: ")
        match ops:
            case "1":
                add_book(books_compendium)
            case "2":
                if not books_compendium:
                    print("No hay libros...")
                else:
                    counter = 0
                    for book in books_compendium:
                        counter += 1
                        print(f"\n{counter}]", end="")
                        book.book_display()
            case "3":
                if not books_compendium:
                    print("No hay libros en el archivo...")
                else:
                    locked_book = input("Coloque el nombre del libro que quiere eliminar: ")
                    for book in books_compendium:
                        if book.name.lower() == locked_book.lower():
                            print(f"{book.name} ha sido eliminado con éxito")
                            books_compendium.remove(book)
                            break

            case "4":
                key = False
                print("Gracias por usar el programa")
    except Exception as e:
        print(f"Error inesperado: {e}")


