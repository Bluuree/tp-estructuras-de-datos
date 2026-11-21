from datos.gestor_datos import cargar_videojuegos
from estructura.arbol_binario import ArbolBinarioBusqueda
from estructura.heap import MaxHeap
from estructura.Grafo import Grafo

juegos = cargar_videojuegos()

arbol = ArbolBinarioBusqueda()

heap = MaxHeap()

grafo = Grafo()

grafo_estudio = Grafo()

for juego in juegos:
    arbol.insertar(juego)
    heap.insertar(juego)
    grafo.agregar_vertice(juego)
    grafo_estudio.agregar_vertice(juego)
    

for juego1 in juegos:
    for juego2 in juegos:
        if juego1.nombre != juego2.nombre:
            if juego1.genero.nombre == juego2.genero.nombre:
                grafo.agregar_arista(juego1,juego2)
            if juego1.estudio.lower() == juego2.estudio.lower():
                grafo_estudio.agregar_arista(juego1,juego2)


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


def filtrar_genero():

    genero = input("Ingrese el género: ")

    encontrado = False

    for juego in juegos:

        if juego.genero.nombre.lower() == genero.lower():

            print(juego)

            encontrado = True

    if not encontrado:
        print("No se encontraron videojuegos de ese género.")
    pass

def filtrar_año():

    anio = int(input("Ingrese el año: "))

    encontrado = False

    for juego in juegos:

        if juego.anio == anio:
            print(juego)
            encontrado = True

    if not encontrado:
        print("No se encontraron videojuegos de ese año.")
    pass

def filtrar_rango():
    anio_menor = int(input(" Desde el : "))
    anio_mayor = int(input(" Hasta el : "))

    encontrado = False
    for juego in juegos:
        if juego.anio >= anio_menor and juego.anio <= anio_mayor:
            print(juego)
            encontrado = True
    if not encontrado:
        print("No se encontraron videojuegos de ese año.")
    pass

def menu_filtar():

    while True:

        print("""
==============================
        VIDEOJUEGOS
==============================
1. Filtar por GENERO
2. Filtrar por AÑO
3. Filtrar por RANGO DE AÑOS
0. Volver
==============================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            filtrar_genero()

        elif opcion == "2":
            filtrar_año()
        
        elif opcion == "3":
            filtrar_rango()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def mostrar_top_rating():

    print("\n⭐ TOP 5 VIDEOJUEGOS CON MAYOR RATING ⭐\n")

    mejores = heap.obtener_top_n(5)

    if not mejores:
        print("No hay videojuegos cargados.")
        return

    for posicion, juego in enumerate(mejores, start=1):
        print(f"{posicion}. {juego.nombre} ⭐ {juego.raiting}")

def top_5_por_genero():

    genero = input("Ingrese el género: ")

    heap_genero = MaxHeap()

    for juego in juegos:
        if juego.genero.nombre.lower() == genero.lower():
            heap_genero.insertar(juego)

    mejores = heap_genero.obtener_top_n(5)

    print(f"\n⭐ TOP 5 {genero.upper()} ⭐\n")

    for i, juego in enumerate(mejores, 1):
        print(f"{i}. {juego.nombre} ⭐ {juego.raiting}")

def menu_top_5():

    while True:

        print("""
==============================
        TOP 5 VIDEOJUEGOS
==============================
1. Top 5 biblioteca completa
2. Top 5 por género
0. Volver
==============================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_top_rating()

        elif opcion == "2":
            top_5_por_genero()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def juegos_relacionados_genero():

    nombre = input("Ingrese el nombre del videojuego: ")

    juego = arbol.buscar(nombre)

    if juego is None:
        print("No se encontró el videojuego.")
        return

    grafo.mostrar_vecinos(juego)

def juegos_relacionados_desarollador():

    nombre = input("Ingrese el nombre de algun videojuego de la desarolladora que busca: ")

    juego = arbol.buscar(nombre)

    if juego is None:
        print("No se encontró el videojuego.")
        return

    grafo_estudio.mostrar_vecinos(juego)

def menu_grafos():

    while True:

        print("""
==============================
        VIDEOJUEGOS RELACIONADOS
==============================
1. Buscar por mismo GENERO
2. Buscar por misma DESAROLLADORA
0. Volver
==============================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            juegos_relacionados_genero()

        elif opcion == "2":
            juegos_relacionados_desarollador()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


def salir():
    print("\n¡Hasta luego!")


MENU = {
    "1": ("Listar videojuegos", listar),
    "2": ("Buscar videojuego", buscar),
    "3": ("Filtrar videojuegos", menu_filtar),
    "4": ("Top 5 videojuegos", menu_top_5),
    "5": ("Buscar Juegos similares", menu_grafos),
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

