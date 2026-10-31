class Genero:
    def __init__(self,nombre: str):
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    
    def __repr__(self) -> str:
        return self._nombre   #Retorna el Genero del videojuego
    
    def __eq__(self, otro):
        if not isinstance(otro, Genero):
            return False

        return self.nombre == otro.nombre

    def __hash__(self):
        return hash(self.nombre)

    


    
    
    