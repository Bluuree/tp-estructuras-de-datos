from collections import deque


class Grafo:

    def __init__(self):
        self.adyacencia = {}


    def agregar_vertice(self, videojuego):
        if videojuego not in self.adyacencia:
            self.adyacencia[videojuego] = []


    def agregar_arista(self, videojuego1, videojuego2):
        self.adyacencia[videojuego1].append(videojuego2)

# ==========================
    # BFS - Busqueda en anchura
    # ==========================

    def bfs(self, inicio):
        visitados = set()
        cola = deque()

        recorrido = []

        cola.append(inicio)
        visitados.add(inicio)

        while cola:

            actual = cola.popleft()

            recorrido.append(actual)

            for vecino in self.adyacencia.get(actual, []):

                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return recorrido



    # ==========================
    # DFS - Busqueda en profundidad
    # ==========================

    def dfs(self, inicio):

        visitados = set()
        recorrido = []

        self._dfs_recursivo(
            inicio,
            visitados,
            recorrido
        )

        return recorrido



    def _dfs_recursivo(self, actual, visitados, recorrido):

        visitados.add(actual)

        recorrido.append(actual)


        for vecino in self.adyacencia.get(actual, []):

            if vecino not in visitados:

                self._dfs_recursivo(
                    vecino,
                    visitados,
                    recorrido
                )

# Estructuras no Utilizadas.
