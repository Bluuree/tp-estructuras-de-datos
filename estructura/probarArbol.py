from .arbol_binario import ArbolBinarioBusqueda
from datos.gestor_datos import cargar_videojuegos

juegos = cargar_videojuegos()

arbol = ArbolBinarioBusqueda()

for juego in juegos:
    arbol.insertar(juego)

resultado = arbol.buscar("Minecraft")
print(resultado)

print("===== INORDER =====")
arbol.inorder()

print("\n===== PREORDER =====")
arbol.preorden()

print("\n===== POSTORDER =====")
arbol.postorden()