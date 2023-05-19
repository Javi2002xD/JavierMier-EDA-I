class Libro:
    def __init__(self, titulo, id):
        self.titulo = titulo
        self.id = id


def agregar_libro(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    id = len(biblioteca) + 1
    libro = Libro(titulo, id)
    biblioteca.append(libro)
    print("Se agrego correctamente.")


def eliminar_libro(biblioteca):
    titulo = input("Ingrese el título del libro que desea eliminar: ")
    for libro in biblioteca:
        if libro.titulo == titulo:
            biblioteca.remove(libro)
            print("Libro eliminado correctamente.")
            return
    print("El libro no se encontró en la biblioteca.")


def ordenar_biblioteca(biblioteca):
    opcion = input("Seleccione el criterio de ordenación, 1) ID numérico, 2)Título: ")
    if opcion == "1":
        biblioteca.sort(key=lambda libro: libro.id)
        print("Biblioteca ordenada por ID numérico.")
    elif opcion == "2":
        biblioteca.sort(key=lambda libro: libro.titulo)
        print("Biblioteca ordenada por título.")
    else:
        print("Opción inválida.")


def ver_biblioteca(biblioteca):
    print("Estado actual de la biblioteca:")
    for libro in biblioteca:
        print(f"ID: {libro.id} - Título: {libro.titulo}")


def menu():
    print("Bienvenido a la biblioteca, puede hacer las siguientes operaciones")
    print("1) Agregar libro")
    print("2) Eliminar libro")
    print("3) Ordenar biblioteca")
    print("4) Ver biblioteca")
    print("5) Salir")


biblioteca = []

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_libro(biblioteca)
    elif opcion == "2":
        eliminar_libro(biblioteca)
    elif opcion == "3":
        ordenar_biblioteca(biblioteca)
    elif opcion == "4":
        ver_biblioteca(biblioteca)
    elif opcion == "5":
        print("Gracias")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
