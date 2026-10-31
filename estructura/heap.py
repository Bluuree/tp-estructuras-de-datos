class MaxHeap:
    def __init__(self):
        self.heap = []

    def insertar(self, valor):
        self.heap.append(valor)

        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        """Hace subir el elemento en el índice 'i' hasta su lugar correcto"""
        if i == 0:
            return

        padre = (i - 1) // 2

        if self.heap[i] > self.heap[padre]:
            self.heap[i], self.heap[padre] = self.heap[padre], self.heap[i]
            self._sift_up(padre)
    
    def _sift_down(self, i):
        """Hunde un elemento comparándolo con sus hijos (busca el rating MAYOR)"""
        n = len(self.heap)
        mayor = i
        izq = 2 * i + 1
        der = 2 * i + 2

        if izq < n and self.heap[izq] > self.heap[mayor]:
            mayor = izq

        if der < n and self.heap[der] > self.heap[mayor]:
            mayor = der

        if mayor != i:
            self.heap[i], self.heap[mayor] = self.heap[mayor], self.heap[i]
            self._sift_down(mayor)

    def extraer_maximo(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        maximo = self.heap[0]
        
        self.heap[0] = self.heap.pop()
        
        self._sift_down(0)
        return maximo

    def obtener_top_n(self, cantidad):
        """ Devuelve los elementos con mayor prioridad.
            Al extraerlos, modifica el Heap original. """
        top_resultados = []
        
        for _ in range(cantidad):
            if not self.heap:  
                break
                
            videojuego_mas_alto = self.extraer_maximo()
            top_resultados.append(videojuego_mas_alto)
            
        return top_resultados
    
    def mostrar(self):
        print(self.heap)





