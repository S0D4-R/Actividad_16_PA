books_compendium = []

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    def book_display(self):
        print(f"Libro: {self.name}|Autor: {self.author}|Año de publicación: {self.year}")

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
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                key = False
    except Exception as e:
        print(f"Error inesperado: {e}")

    finally:
        print("Gracias por usar el prgrama")