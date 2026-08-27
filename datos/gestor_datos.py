import json
from models.genero import Genero
from models.juego import videoJuegos


def cargar_videojuegos(ruta_archivo: str = "datos/juegos.json") -> list:
  juegos = []

  try:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
      datos = json.load(archivo)
 
      for item in datos:
        # Se crea el Objeto Juego
        genero_obj = Genero(item["genero"])

        # Instanciamos el Videojuego usando el objeto Genero
        juego_obj = videoJuegos(
            nombre=item["nombre"],
            genero=genero_obj,
            raiting=item["raiting"],
            estudio=item["estudio"],
            año=item["anio"],
        )

        juegos.append(juego_obj)

  except FileNotFoundError:
    print(f"No se encuentra el archivo  {ruta_archivo}")
  except json.JSONDecodeError:
    print("Error el archivo json tiene un formato invalido.")

  return juegos