from datos.gestor_datos import cargar_videojuegos

juegos = cargar_videojuegos()


def listar():
    for juego in juegos:
        print(juego)

def buscar():

    nombre = input("Ingrese el nombre del videojuego: ")

    encontrado = False

    for juego in juegos:

        if juego.nombre.lower() == nombre.lower():

            print(juego)

            encontrado = True

    if not encontrado:
        print("No se encontró ningún videojuego con ese nombre.")
    
    pass


def filtrar():

    genero = input("Ingrese el género: ")

    encontrado = False

    for juego in juegos:

        if juego.genero.nombre.lower() == genero.lower():

            print(juego)

            encontrado = True

    if not encontrado:
        print("No se encontraron videojuegos de ese género.")
    pass


def salir():
    print("\n¡Hasta luego!")


MENU = {
    "1": ("Listar videojuegos", listar),
    "2": ("Buscar videojuego", buscar),
    "3": ("Filtrar videojuegos", filtrar),
    "0": ("Salir", salir)
}


def mostrar_menu():
    print("\n==============================")
    print("      LIBRERIA DE JUEGOS ")
    print("==============================")

    for opcion, (texto, _) in MENU.items():
        print(f"{opcion}. {texto}")

    print("==============================")


def iniciar():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        accion = MENU.get(opcion)

        if accion is None:
            print("\nOpción inválida.")
            continue

        _, funcion = accion

        funcion()

        if opcion == "0":
            break