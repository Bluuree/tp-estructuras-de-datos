from datos.gestor_datos import cargar_videojuegos

lista_juegos = cargar_videojuegos()
for juego in lista_juegos:
  print(juego)