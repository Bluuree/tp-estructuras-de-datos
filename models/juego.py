class videoJuegos():
    def __init__(self,nombre,genero:Genero,raiting:float,estudio,año: int):
        self._nombre = nombre
        self._genero = genero
        self._estudio = estudio
        self._año = año
        self.raiting = raiting

        

                              #GETTERS 
    @property
    def nombre(self) -> str:
        return self._nombre
    @property
    def genero(self) -> str:
        return self._genero
    @property
    def año (self) -> int:
        return self._año
    @property
    def estudio (self) -> str:
        return self._estudio 
    @property
    def raiting(self) -> float:
        return self._raiting

                                    #SETTERS

    
    @raiting.setter
    def raiting(self,nuevo_raiting) -> float:
        if 0.0 <= nuevo_raiting <= 10.0:
            self._raiting = nuevo_raiting
        else:
            raise ValueError("El rating debe estar entre 0.0 y 10.0")


    
    def __repr__(self) -> str:
        return f"👾 Videojuego: {self._nombre} , 🕹️ Genero: {self._genero} , ⭐ Raiting: {self._raiting} , 👨‍💻 Desarrollador: {self._estudio} , 🗓️Año {self._año}"