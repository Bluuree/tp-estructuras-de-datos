# Diagrama de Clases del Sistema

## 1. Descripción general

El sistema está compuesto por clases de dominio que representan los
videojuegos y sus géneros, y por estructuras de datos encargadas de
realizar búsquedas, rankings y relaciones.

La clase principal del dominio es `videoJuegos`, ya que sus objetos son
utilizados por todas las estructuras principales.

# 2. Diagrama UML de clases
+----------------+
|    Genero      |
+----------------+
| - nombre       |
+----------------+
| + nombre()     |
+----------------+
|
|
| pertenece a
|
↓

+----------------------------+
|       videoJuegos          |
+----------------------------+
| - nombre                   |
| - genero                   |
| - rating                   |
| - estudio                  |
| - anio                     |
+----------------------------+
| + getters                  |
| + setters                  |
| + comparar rating          |
+----------------------------
         |
         |
         | utiliza
         |
         +--------------------+
         |                    |
         ↓                    ↓
+----------------------+    +----------------+
| ArbolBinarioBusqueda |    |    MaxHeap     |
+----------------------+    +----------------+
| - raiz               |    | - heap         |
+----------------------+    +----------------+
| + insertar()         |    | + insertar()   |
| + buscar()           |    | + extraerMax() |
+----------------------+    | + obtenerTop() |
+----------------+
+----------------+
|     Grafo      |
+----------------+
| - adyacencia   |
+----------------+
| + agregarNodo()|
| + agregarArista|
| + mostrarVecinos|
+----------------+


---

# 3. Descripción de clases

---

## Clase videoJuegos

### Responsabilidad

Representar cada videojuego del sistema.

### Atributos principales

| Atributo | Tipo |
|-|-|
| nombre | String |
| genero | Genero |
| rating | Float |
| estudio | String |
| anio | Integer |

### Funciones principales

- Obtener información del videojuego.
- Validar rating.
- Permitir comparación para el Heap.

---

## Clase Genero

### Responsabilidad

Representar el género asociado a un videojuego.

### Atributos

| Atributo | Tipo |
|-|-|
| nombre | String |

### Funciones principales

- Comparar géneros.
- Identificar categorías de videojuegos.

---

# Clases de estructuras de datos

---

## Clase ArbolBinarioBusqueda

### Responsabilidad

Permitir búsquedas eficientes de videojuegos mediante su nombre.

### Relación

Contiene objetos `Nodo`.

Cada nodo almacena un objeto `videoJuegos`.

### Funciones principales

- Insertar videojuegos.
- Buscar videojuegos por nombre.


---

## Clase Nodo

### Responsabilidad

Representar cada elemento dentro del árbol.

### Atributos

| Atributo | Tipo |
|-|-|
| videojuego | videoJuegos |
| izquierdo | Nodo |
| derecho | Nodo |

---

## Clase MaxHeap

### Responsabilidad

Organizar videojuegos según su rating para obtener rankings.

### Funciones principales

- Insertar videojuegos.
- Mantener prioridad máxima.
- Obtener Top N videojuegos.


---

## Clase Grafo

### Responsabilidad

Representar relaciones entre videojuegos.

### Relaciones implementadas

- Mismo género.
- Misma desarrolladora.

### Funciones principales

- Agregar vértices.
- Crear conexiones.
- Mostrar videojuegos relacionados.

# 4. Relaciones entre clases
Genero
|
|
↓
videoJuegos

videoJuegos
|
|
+----> Nodo ----> ArbolBinarioBusqueda
  |
  |
  +----> MaxHeap

  |
  |
  +----> Grafo

# 5. Arquitectura general
            Datos JSON
                |
                ↓
         Gestor de datos
                |
                ↓
          videoJuegos
                |
 --------------------------------
 |              |               |
 ↓              ↓               ↓
 Árbol ABB       MaxHeap          Grafo
 Búsqueda       Ranking        Relaciones
 
