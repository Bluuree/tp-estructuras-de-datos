class Grafo:

    def __init__(self):
        self.adyacencia = {}
    
    def agregar_vertice(self, videojuego):
        if videojuego not in self.adyacencia:
            self.adyacencia[videojuego] = []
    
    def agregar_arista(self, juego1, juego2):

        if juego2 not in self.adyacencia[juego1]:
            self.adyacencia[juego1].append(juego2)

        if juego1 not in self.adyacencia[juego2]:
            self.adyacencia[juego2].append(juego1)
    
    def mostrar_vecinos(self, videojuego):
        if videojuego not in self.adyacencia:
            print("El videojuego no tiene conexiones.")
            return
        
        print(f"\n🎮 Juegos relacionados con {videojuego.nombre}:\n")
        
        for vecino in self.adyacencia[videojuego]:
            print(f"- {vecino.nombre}")