from datos.gestor_datos import cargar_videojuegos
from estructura.arbol_binario import ArbolBinarioBusqueda
from estructura.heap import MaxHeap
from estructura.Grafo import Grafo

juegos = cargar_videojuegos()

arbol = ArbolBinarioBusqueda()

heap = MaxHeap()

grafo = Grafo()

for juego in juegos:
    arbol.insertar(juego)
    heap.insertar(juego)
    grafo.agregar_vertice(juego)

for juego1 in juegos:
    for juego2 in juegos:

        if juego1.nombre != juego2.nombre:

            if juego1.genero.nombre == juego2.genero.nombre:
                
                grafo.agregar_arista(juego1,juego2)





def listar():
    for juego in juegos:
        print(juego)

def buscar():

    nombre = input("Ingrese el nombre del videojuego: ")

    resultado = arbol.buscar(nombre)

    if resultado is None:
        print("No se encontró el videojuego.")
    else:
        print(resultado)
    
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

def mostrar_top_rating():

    print("\n⭐ TOP 5 VIDEOJUEGOS CON MAYOR RATING ⭐\n")

    mejores = heap.obtener_top_n(5)

    if not mejores:
        print("No hay videojuegos cargados.")
        return

    for posicion, juego in enumerate(mejores, start=1):
        print(f"{posicion}. {juego.nombre} ⭐ {juego.raiting}")

def juegos_relacionados():

    nombre = input("Ingrese el nombre del videojuego: ")

    juego = arbol.buscar(nombre)

    if juego is None:
        print("No se encontró el videojuego.")
        return

    grafo.mostrar_vecinos(juego)


def salir():
    print("\n¡Hasta luego!")


MENU = {
    "1": ("Listar videojuegos", listar),
    "2": ("Buscar videojuego", buscar),
    "3": ("Filtrar videojuegos", filtrar),
    "4": ("Top 5 videojuegos", mostrar_top_rating),
    "5": ("Buscar Juegos similares", juegos_relacionados),
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

