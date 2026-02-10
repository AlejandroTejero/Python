# Python (apuntes + prácticas)

Repositorio de **prácticas en Python** organizadas por ejercicios, hojas y temas. La idea no es tener “un proyecto final”, sino un **historial de aprendizaje**: desde fundamentos del lenguaje hasta estructuras de datos, sockets y concurrencia.

> Nota: los nombres de archivos (ej1.py, HojaX.py, IntentoX.py, etc.) reflejan ejercicios de clase/repaso y distintos intentos de solución.

---

## Estructura del repo

A nivel general encontrarás:

- `Practicas/`
  - `EjerciciosClase/`: ejercicios cortos de clase y repaso.
  - `EjPorTemas/`: ejercicios agrupados por tema (T1, T2, T3…).
  - `EjFinal/`: prácticas más completas de estructuras de datos, sockets y concurrencia.

---

## Contenido por carpetas

### `Practicas/EjerciciosClase/`
Ejercicios “unitarios” para practicar conceptos del lenguaje y resolver problemas típicos:

- Variables, tipos y operadores.
- Condicionales y bucles.
- Funciones (parámetros, retorno, reutilización).
- Listas / diccionarios y recorrido de colecciones.
- Ejercicios tipo examen/repaso (`EjExamen.py`, `Repaso.py`, `Hoja1.py`…).
- Ejemplos de **algoritmos sencillos** y simulación (p. ej. aproximaciones tipo *Monte Carlo*).
- Scripts con lógica práctica (p. ej. inventarios, filtros, cálculos, etc.).

### `Practicas/EjPorTemas/`
Carpeta pensada para estudiar por bloques:

- `T1/`: fundamentos y ejercicios de base (control de flujo, colecciones, funciones).
- `T2/`: **POO** (programación orientada a objetos): clases, atributos/métodos, encapsulación, y organización.
- `T3/`: **cliente/servidor** básico (introducción a sockets).

### `Practicas/EjFinal/`
Bloque más “de sistemas” y estructuras de datos (más cercano a prácticas completas):

#### Estructuras de datos
- `Pilas/` (stacks) y `Colas/` (queues) implementadas de varias formas:
  - Con listas de Python (enfoque rápido).
  - Con nodos/listas enlazadas (enfoque estructurado).
- `Listas/`:
  - Lista enlazada simple y doblemente enlazada.
- `Arboles/`:
  - Árbol binario y **árbol binario de búsqueda** (BST).
  - Apoyo con estructuras auxiliares (p. ej. `Stack.py`).

#### Colecciones
- `Colecciones/` contiene subcarpetas de apoyo/repaso sobre pilas y colas.

#### Sockets
- `Sockets/`, `Sockets_teoria/`, `Sockets_repaso/` y `Sockets_practica/`:
  - Ejemplos de **TCP cliente/servidor**.
  - Comunicación entre procesos y envío/recepción de datos.
  - Serialización en algunos ejercicios (p. ej. con `pickle`) para enviar estructuras.

#### Concurrencia
- `Concurrencia/` (Teoría / Práctica / Intentos):
  - Introducción a **hilos** (`threading`), temporización (`time`) y ejecución concurrente.
  - Ejercicios típicos de lanzar tareas, coordinar ejecuciones y entender el flujo.

---

## Contenidos

**Fundamentos de Python**
- Sintaxis, tipos, operadores, control de flujo.
- Funciones y modularización.
- Manejo de colecciones (listas, diccionarios, tuplas).

**POO**
- Definición de clases, métodos, constructores.
- Diseño básico orientado a objetos para modelar problemas.

**Estructuras de datos**
- Implementación y uso de pilas, colas, listas enlazadas y árboles (incluyendo BST).
- Operaciones típicas: inserción, borrado, recorrido, búsqueda, etc.

**Red y sistemas**
- Programación con sockets (cliente/servidor TCP).
- Envío de datos entre procesos (y serialización cuando aplica).

**Concurrencia**
- Uso de hilos con `threading`.
- Ejecución concurrente y nociones de sincronización/tiempos.

---

## Cómo ejecutar los ejercicios

No hay un “main” único: cada archivo suele ser ejecutable por separado.

```bash
python3 ruta/al/archivo.py
```

```bash 
python3 Practicas/EjFinal/Sockets/servidor.py
python3 Practicas/EjFinal/Sockets/servidor.py
```