# Casos de Uso del Sistema

## 1. Diagrama de casos de uso

                 +----------------+
                 |    Usuario     |
                 +----------------+
                         |
                         |
    ---------------------------------------------
    |            |            |          |        |
    ↓            ↓            ↓          ↓        ↓
   listar    buscar      filtar    ver Top    Consultar
                         |
                         ↓

                Biblioteca de
                videojuegos

---

# 2. Actores

## Usuario

Persona que utiliza el sistema para consultar información sobre videojuegos,
realizar búsquedas, obtener rankings y explorar relaciones entre videojuegos.

---

# 3. Casos de uso

---

# Caso de uso 1: Listar videojuegos

## Actor

Usuario

## Objetivo

Visualizar todos los videojuegos disponibles en la biblioteca.

## Precondición

El archivo de datos debe encontrarse cargado correctamente.

## Flujo principal

1. El usuario selecciona la opción "Listar videojuegos".
2. El sistema recorre la lista de videojuegos cargados.
3. El sistema muestra la información de cada videojuego:
   - Nombre.
   - Género.
   - Rating.
   - Desarrolladora.
   - Año.

## Flujo alternativo

Si no existen videojuegos cargados, el sistema no muestra resultados.

## Postcondición

El usuario puede visualizar la información de la biblioteca.

---

# Caso de uso 2: Buscar videojuego

## Actor

Usuario

## Objetivo

Encontrar un videojuego específico mediante su nombre.

## Precondición

La biblioteca debe estar cargada y el árbol binario debe estar construido.

## Flujo principal

1. El usuario selecciona "Buscar videojuego".
2. El sistema solicita el nombre del videojuego.
3. El usuario ingresa el nombre.
4. El sistema realiza la búsqueda utilizando el Árbol Binario de Búsqueda.
5. El sistema muestra el videojuego encontrado.

## Flujo alternativo

Si el videojuego no existe, el sistema informa que no fue encontrado.

## Postcondición

El usuario obtiene la información del videojuego solicitado.

---

# Caso de uso 3: Filtrar videojuegos

## Actor

Usuario

## Objetivo

Encontrar videojuegos según determinados criterios.

## Precondición

La biblioteca debe estar cargada.

## Flujo principal

1. El usuario selecciona la opción "Filtrar videojuegos".
2. El sistema muestra las opciones disponibles:
   - Filtrar por género.
   - Filtrar por año.
   - Filtrar por rango de años.
3. El usuario selecciona un criterio.
4. El sistema muestra los videojuegos que cumplen la condición.

## Flujo alternativo

Si no existen videojuegos que coincidan con el filtro, el sistema informa
que no se encontraron resultados.

## Postcondición

El usuario obtiene un listado filtrado.

---

# Caso de uso 4: Consultar Top 5 videojuegos

## Actor

Usuario

## Objetivo

Obtener los videojuegos con mayor rating.

## Precondición

La biblioteca debe contener videojuegos con rating válido.

## Flujo principal

1. El usuario selecciona "Top 5 videojuegos".
2. El sistema utiliza un Heap máximo.
3. El sistema extrae los videojuegos con mayor prioridad.
4. El sistema muestra los 5 videojuegos con mayor rating.

## Flujo alternativo

Si no existen videojuegos cargados, el sistema informa que no hay resultados.

## Postcondición

El usuario obtiene un ranking ordenado por rating.

---

# Caso de uso 5: Consultar videojuegos relacionados

## Actor

Usuario

## Objetivo

Encontrar videojuegos relacionados con otro videojuego.

## Precondición

El grafo de relaciones debe estar construido.

## Flujo principal

1. El usuario selecciona "Buscar juegos similares".
2. El sistema solicita el nombre de un videojuego.
3. El usuario ingresa un videojuego.
4. El sistema busca sus conexiones en el grafo.
5. El sistema muestra videojuegos relacionados.

## Relaciones disponibles

- Mismo género.
- Misma desarrolladora.

## Flujo alternativo

Si el videojuego no existe, el sistema informa que no fue encontrado.

## Postcondición

El usuario obtiene videojuegos relacionados.
