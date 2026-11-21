# Documento de Requerimientos

## 1. Descripción general

El proyecto consiste en una biblioteca de videojuegos desarrollada en Python.
El sistema permite gestionar información de videojuegos, realizar búsquedas,
filtrar datos, obtener rankings y consultar relaciones entre videojuegos
utilizando diferentes estructuras de datos.

Los datos son cargados desde un archivo JSON y transformados en objetos
VideoJuego, los cuales son utilizados por las diferentes estructuras del sistema.

---

# 2. Requerimientos funcionales

## RF01 - Carga de videojuegos

El sistema debe permitir cargar los videojuegos almacenados en un archivo
JSON y transformarlos en objetos utilizables dentro de la aplicación.


## RF02 - Listado de videojuegos

El sistema debe permitir visualizar todos los videojuegos disponibles
mostrando su información principal:

- Nombre
- Género
- Rating
- Desarrolladora
- Año


## RF03 - Búsqueda de videojuegos

El sistema debe permitir buscar un videojuego mediante su nombre.

La búsqueda debe realizarse utilizando un Árbol Binario de Búsqueda,
organizado según el nombre del videojuego.


## RF04 - Filtrado de videojuegos

El sistema debe permitir filtrar videojuegos según diferentes criterios:

- Género
- Año específico
- Rango de años


## RF05 - Ranking de videojuegos

El sistema debe permitir consultar los videojuegos con mayor rating.

El ranking debe utilizar un Heap máximo para obtener los mejores videojuegos.


## RF06 - Ranking por género

El sistema debe permitir obtener un Top 5 de videojuegos pertenecientes
a un género específico.


## RF07 - Consulta de videojuegos relacionados

El sistema debe permitir consultar videojuegos relacionados mediante grafos.

Las relaciones disponibles son:

- Videojuegos del mismo género.
- Videojuegos de la misma desarrolladora.


## RF08 - Interacción mediante menú

El usuario debe poder acceder a las funcionalidades del sistema mediante
una interfaz de terminal con opciones seleccionables.


---

# 3. Requerimientos no funcionales


## RNF01 - Lenguaje de desarrollo

El sistema debe estar desarrollado utilizando Python.


## RNF02 - Uso de estructuras de datos

Las estructuras principales deben ser implementadas manualmente,
sin depender de librerías externas de estructuras.


## RNF03 - Organización del código

El proyecto debe mantener una separación clara entre:

- Modelos.
- Datos.
- Estructuras.
- Interfaz de usuario.


## RNF04 - Mantenibilidad

El código debe estar organizado de manera modular permitiendo agregar
nuevas funcionalidades sin modificar completamente el sistema.


## RNF05 - Correctitud de datos

Los videojuegos deben mantener información válida, especialmente el rating,
que debe encontrarse dentro del rango permitido.


---

# 4. Alcance del sistema

El sistema permite administrar una biblioteca de videojuegos mediante
estructuras de datos propias.

Incluye:

- Carga de información desde archivos JSON.
- Búsqueda eficiente por nombre.
- Filtrado de videojuegos.
- Ranking mediante Heap.
- Relaciones entre videojuegos mediante Grafos.
- Interacción mediante terminal.


---

# 5. Fuera de alcance

El sistema no contempla:

- Registro de usuarios.
- Sistema de autenticación.
- Base de datos externa.
- Conexión con servicios online.
- Compra o descarga de videojuegos.
- Actualización automática de información desde internet.


---

# 6. Usuarios del sistema

El sistema está pensado para un único tipo de usuario:

## Usuario general

Puede consultar la biblioteca de videojuegos, realizar búsquedas,
observar rankings y explorar relaciones entre videojuegos.