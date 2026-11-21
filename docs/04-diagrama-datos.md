# Diagrama de conexión entre estructuras de datos

## 1. Descripción general

El sistema utiliza diferentes estructuras de datos para resolver distintas
necesidades del usuario.

Los datos originales son cargados desde un archivo JSON y transformados en
objetos `videoJuegos`. Estos objetos son utilizados simultáneamente por
distintas estructuras especializadas.

Cada estructura tiene una responsabilidad específica:

- Árbol Binario de Búsqueda: búsqueda por nombre.
- Heap Máximo: ranking por rating.
- Grafo: relaciones entre videojuegos.

# 2. Diagrama general del flujo de datos

                videojuegos.json
                       |
                       |
                       ↓

             Gestor de datos
             (cargar_videojuegos)

                       |
                       |
                       ↓

          Lista de objetos videoJuegos


                       |
    -----------------------------------------
    |                 |                     |
    ↓                 ↓                     ↓
    Árbol Binario        MaxHeap              Grafos

 (nombre)            (rating)           (relaciones)
     |                 |                     |

    ↓                 ↓                     ↓
    Buscar juego       Obtener Top 5       Juegos relacionados
                                             |
                                         |
                       ------------------
                       |
                       ↓

             Interfaz de terminal

# 3. Descripción de las conexiones


## Archivo JSON

Contiene la información inicial de los videojuegos.

Cada registro incluye datos como:

- Nombre.
- Género.
- Rating.
- Desarrolladora.
- Año.

## Gestor de datos

Responsabilidad:

- Leer el archivo JSON.
- Crear objetos de tipo `videoJuegos`.
- Crear objetos asociados de tipo `Genero`.
- Entregar la lista cargada al sistema.

## Lista de objetos videoJuegos

Es la representación principal de los datos dentro del programa.

Cada objeto contiene toda la información necesaria para ser utilizado
por las diferentes estructuras.


# 4. Estructuras utilizadas


## Árbol Binario de Búsqueda

### Organización

Los videojuegos se almacenan ordenados por nombre.

### Uso dentro del sistema

Permite:

- Buscar videojuegos específicos.
- Reducir la cantidad de comparaciones necesarias.

## MaxHeap

### Organización

Los videojuegos se ordenan según su rating.

### Uso dentro del sistema

Permite:

- Obtener los videojuegos con mayor puntuación.
- Generar rankings Top 5.


## Grafo

### Organización

Cada videojuego representa un vértice.

Las conexiones representan relaciones entre videojuegos.

### Relaciones utilizadas

- Mismo género.
- Misma desarrolladora.

# 5. Flujo de una consulta


Ejemplo: Buscar videojuegos relacionados

Usuario

  ↓

Ingresa videojuego

  ↓

Árbol Binario

  ↓

Encuentra objeto videoJuego

  ↓

Grafo

  ↓

Busca conexiones

  ↓

Muestra videojuegos relacionados

# 6. Arquitectura final
             DATOS

        videojuegos.json

                ↓


          PROCESAMIENTO

         Gestor de datos

                ↓


           OBJETOS

         videoJuegos


                ↓
---------------------------------

↓               ↓              ↓
ABB            Heap           Grafo

 Buscar        Ranking       Relaciones
 ---------------------------------
                ↓


         Terminal Usuario

# Algoritmos adicionales implementados

Además de las funcionalidades utilizadas por el sistema,
se desarrollaron algoritmos complementarios asociados a la estructura
de grafos.

Estos algoritmos incluyen:

- BFS (Breadth First Search).
- DFS (Depth First Search).
- Búsqueda de caminos mínimos.

Actualmente estos algoritmos no se encuentran conectados a la interfaz
de usuario, ya que las funcionalidades requeridas fueron resueltas mediante
las consultas de relaciones directas entre videojuegos.

Su implementación queda disponible para futuras extensiones del sistema.