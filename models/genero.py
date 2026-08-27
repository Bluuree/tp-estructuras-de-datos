class Genero:
    def __init__(self,nombre: str):
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    
    def __repr__(self) -> str:
        return self._nombre   #Retorna el Genero del videojuego

    


    
    
    