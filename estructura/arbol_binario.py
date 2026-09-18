
class Nodo:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierdo = None
        self.derecho = None
    

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, videojuego):
        if self.raiz is None :
            self.raiz = Nodo(videojuego)
        else : self._insertar_recursivo(self.raiz, videojuego)

    def _insertar_recursivo(self, nodo_actual, videojuego):
        if videojuego.nombre < nodo_actual.videojuego.nombre:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(videojuego)
            else:
                  self._insertar_recursivo(nodo_actual.izquierdo, videojuego)
        
        elif videojuego.nombre > nodo_actual.videojuego.nombre :
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(videojuego)

            else:
                  self._insertar_recursivo(nodo_actual.derecho, videojuego)
    
    def buscar(self, nombre, ):
        if self.raiz is None:
            print("no existe el video juego")
        
        elif self.raiz.videojuego.nombre == nombre:
            return self.raiz.videojuego
        else: 
            return self._busqueda_recursiva(self.raiz, nombre)


    def _busqueda_recursiva(self, nodo_actual, nombre):
        if nodo_actual is None:
             return None
             
        if nombre == nodo_actual.videojuego.nombre:
                  return nodo_actual.videojuego

        if nombre < nodo_actual.videojuego.nombre:
               return self._busqueda_recursiva(nodo_actual.izquierdo , nombre)

        elif nombre > nodo_actual.videojuego.nombre:
                return self._busqueda_recursiva(nodo_actual.derecho , nombre)
