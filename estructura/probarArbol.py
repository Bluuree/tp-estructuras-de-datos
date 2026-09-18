from .arbol_binario import ArbolBinarioBusqueda
from datos.gestor_datos import cargar_videojuegos

juegos = cargar_videojuegos()

arbol = ArbolBinarioBusqueda()

for juego in juegos:
    arbol.insertar(juego)

resultado = arbol.buscar("Minecraft")
resultado2 = arbol.buscar("League of Legends")
print(resultado, resultado2)