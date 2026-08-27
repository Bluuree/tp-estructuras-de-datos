from models.genero import Genero
from models.juego import videoJuegos

print("Prueba de models")

            #Instacia de Clases                         
genero_rpg = Genero("RPG")
juego_valido = videoJuegos(
    nombre="Red Dead Redemption 2",
    genero=genero_rpg,
    raiting=9.8,
    estudio="Rockstar Games",
    año= 2018,
)

print("\n✅ Impresión del objeto válido (__repr__):")
print(juego_valido)

                    #Probar la validacion  de setters
print("\n Probrando la seguridad del setter con rating mayor a 10:")
try:
  juego_invalido = videoJuegos(
      nombre="Juego Bugueado",
      genero=genero_rpg,
      raiting=15.0,     
      estudio="Indie Studio",
      año= 2024,
  )
except ValueError as error:
  print(f" Capturado correctamente: {error}")

print("\n---  PRUEBAS FINALIZADAS ---")