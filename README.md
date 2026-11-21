# 🎮 Biblioteca de Videojuegos - Trabajo Práctico Estructuras de Datos

## 📌 Descripción

Este proyecto de EDD para la Universidad Nacional Guillermo Brown consiste en una *BIBLIOTECA* de videojuegos desarrollada en Python como trabajo práctico para la materia **Estructuras de Datos** COMISION 3 GRUPO 6.

El programa permite administrar una colección de videojuegos cargados desde un archivo JSON, utilizando diferentes estructuras de datos como Arboles, Heaps y Grafos para realizar búsquedas, filtros, rankings.

El objetivo principal es aplicar estructuras de datos vistas durante la cursada en un caso práctico y funcional.


## 🚀 Instalación y ejecución

## Requisitos

- Python 3.x instalado.
- No requiere librerías externas.

## Ejecución

```bash
1. Clonar el repositorio:

git clone https://github.com/Bluuree/tp-estructuras-de-datos/commits/main/

2. Accerder a la Carpeta del Proyecto

cd tp-estructuras-de-datos:

3. Ejecutar el Programa:

python main.py
```

## 🕹️ Tutorial de uso

Al inicar el Programa vera un MENU principal
==============================
      LIBRERIA DE JUEGOS
==============================
1. Listar videojuegos
2. Buscar videojuego
3. Filtrar videojuegos
4. Top 5 videojuegos
5. Buscar Juegos similares
0. Salir
==============================

1. Listar videojuegos
Muestra todos los videojuegos disponibles en la biblioteca junto con su información:
- Nombre
- Género
- Rating
- Desarrolladora
- Año de lanzamiento

2. Buscar videojuego
Permite buscar un videojuego específico ingresando su nombre.
La búsqueda no distingue entre mayúsculas y minúsculas.

3. Filtrar videojuegos
Permite obtener videojuegos según diferentes criterios, como Filtar por GENERO, AÑO y RANGO de AÑOS

4. Top 5 videojuegos
Permite obtener rankings utilizando un Heap.

Opciones:
- Top 5 de toda la biblioteca.
- Top 5 por género.

5. Buscar juegos similares
Permite encontrar videojuegos relacionados mediante grafos.

El programa cuenta con dos tipos de relaciones:
- Relación por géneroBusca 
  videojuegos que compartan el mismo género.
- Relacion por Desarolladora
  videojuegos que comparten desarollador.

## 🌳 Estructuras de Datos implementadas

Árbol Binario de Búsqueda (BST)
Utilizado para buscar videojuegos rápidamente por nombre.
Heap Máximo
Utilizado para obtener los videojuegos con mayor rating.

Permite generar rankings Top 5.
Grafos
Utilizados para representar relaciones entre videojuegos.

Se implementaron dos grafos:
- Grafo por género.
- Grafo por desarrolladora.

## 📂 Estructura del proyecto

tp-estructuras-de-datos/

│
├── main.py
│
├── datos/
│   ├── videojuegos.json
│   └── gestor_datos.py
│
├── estructura/
│   ├── arbol_binario.py
│   ├── heap.py
│   └── Grafo.py
│
├── models/
│   ├── videojuegos.py
│   └── genero.py
│
└── ui/
    └── terminal.py

## 👥 Integrantes
Luca Pirillo Gonzalez Laureano.
Juan Pablo Jurjo.
Francisco Francon Diaz .

ESTRUCTURAS DE DATOS 2026 COMISION 3 GRUPO 6.
