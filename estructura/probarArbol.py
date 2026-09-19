from .arbol_binario import ArbolBinarioBusqueda
from datos.gestor_datos import cargar_videojuegos

juegos = cargar_videojuegos()

arbol = ArbolBinarioBusqueda()

for juego in juegos:
    arbol.insertar(juego)

resultado = arbol.buscar("Minecraft")
resultado2 = arbol.buscar("League of Legends")
resultado3 = arbol.buscar ("Raibow six siege")

resultados = [
    ("Minecraft", resultado),
    ("League of Legends", resultado2),
    ("Rainbow six siege", resultado3)
    ]
print("Resultados de búsqueda:")

for nombre_buscado, juego in resultados:
    print(f"\nBuscando: '{nombre_buscado}'")
    if juego:
        print(f"Encontrado: {juego}")
    else:
        print("No se encontró el videojuego.")
